#! /usr/bin/python
print "Content-type: text/html"
print 
print "<h1>aaa</h1>"

import cgitb;cgitb.enable()
import MySQLdb,cgi,sys

db = MySQLdb.connect('localhost','root','liulinroot','liulin')

cursor = db.cursor()

form = cgi.FieldStorage()

reply_to = form.getvalue('reply_to')

print """

<html>

	<head>

		<title>compose message</title>

	</head>

	<body>

		<h1>compose message</h1>



		<form action = 'save.cgi' method='post'>

		"""

subject = ''

if reply_to is not None:

	print '<input type="hidden" name="reply_to" value="%s">' % reply_to

	cursor.execute('SELECT subject FROM message WHERE id = %s' % reply_to)

	subject = cursor.fetchone()[0]

	if not subject.startswith('Re:'):

		subject = 'Re:'+subject

print"""

	<b>subject:</b><br />

	<input type='text' size='40' name='subject' value="%s"> </br >



	<b>sender:</b><br />

	<input type='text' size='40' name='sender'> </br >



	<b>message:</b><br />

	<textarea name='text' cols='40' rows='20'></textarea><br>



	<input type='submit' value='save' />

	</form>



	<p><a href='main.cgi'>back to the main page</a></p>

	</body>

<html> 

""" % subject


