#!/usr/bin/python3

import cgi
import subprocess
import webbrowser as wb

print("content-type: text/html")
print()

data= cgi.FieldStorage()
c = data.getvalue("x")
##print (c)
op = subprocess.getoutput("sudo " + c)
print(op)
##if ("start" in c) or ("show" in c) or("date" in c):
##if ('date' in c):
   ## op = subprocess.getoutput(date)
    ##print(op)
##else:
   ## print("Cant process")
print("<br />")
print("<br />")
print("<br />")
print("<br />")
print("<br />")
print("<br />")
