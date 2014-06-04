def deco(func):
    def _deco(*args,**kwargs):
	print("before %s called." % func.__name__)
	ret = func(*args,**kwargs)
	print("after %s called. result: %s" %(func.__name__,ret))
	return ret
    return _deco

@deco
def myfunc(a,b):
    print("myfunc(%s, %s) called called." %(a,b))
    return a+b
@deco
def myfunc2(a,b,c):
    print("myfunc(%s, %s, %s) called called." %(a,b,c))
    return a+b+c

print myfunc(1,2)
print myfunc(2,5)
print myfunc2(1,1,2)
print myfunc2(1,5,2)

	
