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
    w1 = None 
    x1 = None 
    y1 = None 
    z1 = None 
    def __init__(self,w1,x1,y1,z1):
	self.w1 = w1
	self.x1 = x1
	self.y1 = y1
	self.z1 = z1
    def area(self):
	hei = self.w1.y - self.y1.y 
	len = self.x1.x - self.w1.x
	return len * hei 

r = Rectangle(a,b,c,d)

print r.area()
