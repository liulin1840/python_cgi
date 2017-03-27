#! /usr/bin/python
print "Content-type: text/html"
print 


from os.path import join,abspath

import cgi,sys

edit_log = open('edit.log','w+')



BASE_DIR = abspath('data')

form = cgi.FieldStorage()

filename = form.getvalue('filename')

print 'aaaa'
print >>edit_log,'filename ==>%s' % filename

print >>edit_log,'BASE_DIR ==>%s' % BASE_DIR

if not filename:

	print 'please enter a file name'

	sys.exit()

text = open(join(BASE_DIR,filename)).read()

print >>edit_log,'open BASE_DIR,filename ==>%s' % join(BASE_DIR,filename)



print """

<html>

<head>

	<title>Editing...</title>

</head>

<body>

	<form action="save.cgi" method="post">

	<b>File:</b>%s<br/>

	<input type="hidden" value="%s" name='filename'>

	<b>Password:</b><br/>

	<input type="password" name='password'>	<br/>

	<b>Text:</b><br/>

	<textarea rows ='20' cols='40' name='text'>%s</textarea></br>

	<input type='submit' value='Save'>

	</form>

</body>

</html>

""" % (filename,filename,text)
