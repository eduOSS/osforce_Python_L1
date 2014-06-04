def deco(func):
    print 'hello'
    def _deco():
	print("before myfunc() called.")
        print func()
	print("after myfunc() called.")
    return _deco

@deco
def myfunc():
    print("myfunc() called.")
    return 'ok'

myfunc()
myfunc()

