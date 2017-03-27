#! /usr/bin/python
print "Content-type: text/html"
print 
print "<h1>aaa</h1>"

import cgitb;cgitb.enable()

import MySQLdb,cgi,sys

db = MySQLdb.connect('localhost','root','liulinroot','liulin')

cursor = db.cursor()

form = cgi.FieldStorage()

id = form.getvalue('id')

print """

<html>

	<head>

		<title>view message</title>

	</head>

	<body>

		<h1>view message</h1>

		"""

try:id = int(id)

except :

	print 'invalid message id'

	sys.exit()

cursor.execute('SELECT * FROM message WHERE id = %i' % id)

rows = cursor.fetchall()

if not rows:

	print 'unknow message id'

	sys.exit()

row = rows[0]

print"""

	<p><b>subject:</b>%s<br />

		<b>sender:</b>%s<br />

		<pre>%s</pre>

	</p>

	</hr>

	<p><a href='main.cgi'>back to the main page</a></p>

	<p><a href='edit.cgi?reply_to=%s'>reply</a></p>

	</body>

<html>

""" % (row[1],row[2],row[4],row[0])


