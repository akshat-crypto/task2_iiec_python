#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

data1 = cgi.FieldStorage()
admcmd = data1.getvalue("x")

output = subprocess.getoutput(" sudo " + admcmd)
print(output)
