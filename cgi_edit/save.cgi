#! /usr/bin/python
print "Content-type: text/html"
print 
print "<h1>aaa</h1>"

from os.path import join,abspath

import cgi,sys,sha

edit_log = open('edit.log','w+')

BASE_DIR = abspath('data')

form = cgi.FieldStorage()

text = form.getvalue('text')

filename = form.getvalue('filename')

password = form.getvalue('password')

if not (filename and text and password):

	print 'invalid parameter'

	sys.exit()

if sha.sha(password).hexdigest() != '8843d7f92416211de9ebb963ff4ce28125932878':

	print 'invalid password'	

f = open(join(BASE_DIR,filename),'w+')

f.write(text)

f.close()

print 'the file has been saved!'
