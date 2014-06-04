def decomaker(arg):
    def newDeco(func):
	print func,arg
	return func
    return newDeco
@decomaker(deco_args)
def foo():pass
foo()
