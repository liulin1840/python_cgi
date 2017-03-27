#! /usr/bin/python
print "Content-type: text/html"
print 
print "<h1>aaa</h1>"

import cgitb;cgitb.enable()
import MySQLdb,cgi,sys

def quote(string):

	if string:

		return string.replace("'","\\'")

	else:

		return string



db = MySQLdb.connect('localhost','root','liulinroot','liulin')

cursor = db.cursor()



form = cgi.FieldStorage()

sender   = quote(form.getvalue('sender'))

subject  = quote(form.getvalue('subject'))

text     = quote(form.getvalue('text'))

reply_to = quote(form.getvalue('reply_to'))



if not (sender and subject and text):

	print 'please supply sender subject text'

	sys.exit()



if reply_to is not None:

	query = """

	INSERT INTO message(reply_to,sender,subject,text) 

	VALUES ('%i','%s','%s','%s')"""  % (int(reply_to),sender,subject,text)

else:

	query= """

	INSERT INTO message(sender,subject,text)

	VALUES ('%s','%s','%s') """ % 	(sender,subject,text)



cursor.execute(query)

db.commit()



print """

<html>

	<head>

		<title>message save</title>

	</head>

	<body>

		<h1>message save</h1>

		</hr>

	<p><a href='main.cgi'>back to the main page</a></p>

	</body>

<html>

"""
