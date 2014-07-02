import time
def timeit(arg_of_decorator):
    def deco(func):
	def _deco(*args, **kwargs):
            time1 = time.time()
	    print 'time befor function:',time1 
	    print args,kwargs,arg_of_decorator
            func(*args, **kwargs) 
	    time2 = time.time()
	    print 'time after function:', time2 
            print 'time used', time2-time1
	return _deco
    return deco

@timeit('leo')
def myfunc1(a, b):
    print a**b

@timeit('leo')
def myfunc2(a, b,c):
    print a**b*c

myfunc1(35657,2876)
myfunc2(3,4,16)
