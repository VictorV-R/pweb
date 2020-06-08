#!/usr/bin/python3
import sqlite3
import cgi
import cgitb

print("Content-type:text/html\n\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello</h2>")

form = cgi.FieldStorage()

kind = form.getvalue('kind')

conn = sqlite3.connect('imdb.db')
c = conn.cursor()
select = "SELECT * FROM actor"
table = c.execute(select)
for row in table:
    print(row)
print("</p>")
print("</body>")
print("</html>")
