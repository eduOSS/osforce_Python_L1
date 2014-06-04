#!usr/bin/python
#!coding:utf8

def myzip(ls1,ls2,cr):
    le = len(ls1) - len(ls2)
    if le > 0:
	i = le
	while(i>0):
	    ls2.append(cr)
	    i = i - 1
    else:
        i = -le
	while(i>0):
	    ls1.append(cr)
	    i = i - 1
    return zip(ls1,ls2)

a = [4,3,2,6,7,8]
b = [23,45,67]

print myzip(a,b,'r')
print a,b
