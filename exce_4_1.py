#!usr/bin/python
#!coding:utf8

class Point:
    def __init__(self,x=0,y=0):
	self.x = x
	self.y = y

a = Point(1,4)
b = Point(4,4)
c = Point(1,2)
d = Point(4,2)

class Rectangle:
    def __init__(self,a,b,c,d):
	self.a = a
	self.b = b
	self.c = c
	self.d = d
        self.a = Point(4,5)
        a = Point(5,4)
    def area(self):
	hei = a.y - c.y 
	len = b.x - a.x
	return len * hei 
r = Rectangle(a,b,c,d)

print r.area()
print a.x
