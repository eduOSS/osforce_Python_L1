def decorator_func_args(func):
    def handle_args(*arg, **kargs):
        print "begin"
        func(*arg, **kargs)
        print "end"
	return 'hh'
    return handle_args

@decorator_func_args
def foo2(a, b=2):
    print a, b

print foo2(1)
