#! /usr/bin/python
print "Content-type: text/html"
print 
print "<h1>aaa</h1>"
print """
        <html>
        <head>
                <title>File Editor</title>
        </head>
        <body>
                <form action="/cgi-bin/cgi_edit/edit.cgi" method="post">
             	   <b>File Name:</b><br/>
                	<input type="text" name="filename">
                	<input type="submit" value="Open">      
                </form>
        </body>
        </html>
"""  
