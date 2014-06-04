#!/usr/bin/python
#!coding:utf8

import os
import sys
#==== for
for i in range(12):
    if i % 2 == 0:
	print i
    else:
	continue
#==== for else
else:
    print "normal exit"
d = {"name": 2}

#==== try except
try:
    d["n"]
except KeyError:
	print "the key is not ready!"
#==== try else
else:
    print d["name"]

#==== function
def func(s):
    print s
#==== rename fucntion
a = func

a(3)
func("hello")
a(d)

#==== class
class A:
    def __init__(self,number,number2):
	self.number = number
	self.number2 = number2

a = A(10,35)

print a.number, a.number2

#print sys.path
print os.path.dirname(__file__)
