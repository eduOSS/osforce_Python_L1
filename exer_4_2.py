class A(object):
    instance = None
    def __new__(cls,*args,**kwargs):
	print cls.instance
        if not cls.instance:
	    cls.instance = object.__new__(cls,*args,**kwargs)
print id(A())
print id(A())
