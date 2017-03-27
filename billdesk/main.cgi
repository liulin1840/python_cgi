#! /usr/bin/python
print "Content-type: text/html"
print 
print "<h1>aaa</h1>"

import cgitb;cgitb.enable()
import MySQLdb

db = MySQLdb.connect('localhost','root','liulinroot','liulin')
cursor = db.cursor()

print """
<html>
	<head>
		<title>the liulin billdesk</title>
	</head>
	<body>
		<h1>the liulin billdesk</h1>
		"""

cursor.execute('SELECT * FROM message')
rows = cursor.fetchall()
toplevel=[]
children={}

for row in rows:
	parent_id = row[3]
	if parent_id is None:
		toplevel.append(row)
	else:
		children.setdefault(parent_id,[]).append(row)

def format(row):
	print '<p><a href="view.cgi?id=%i"> %s</a></p>' % (row[0],row[1])
	try:kids = children[row[0]]
	except KeyError:pass
	else:
		print '<blockquote>'
		for kid in kids:
			format(kid)
		print '</blockquote>'

print '</p>'

for row in toplevel:
	format(row)

print"""
	</p>
	</hr>
	<p><a href='edit.cgi'> post message</a></p>
	</body>
<html>
"""
