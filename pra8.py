def deco(arg):
    def _deco(func):
            print("before %s called [%s]." %(func.__name__,arg))
	    func()
	    print("after %s called [%s]." %(func.__name__,arg))
    return _deco

@deco("mymodule")
def myfunc():
    print("myfunc() called.")

@deco("module2")
def myfunc2():
    print("myfunc2() called.")

print myfun_myfunc2()

