def decorator_with_params(arg_of_decorator):
    print arg_of_decorator
    def newDecorator(func):
        print func
        return func
    return newDecorator

@decorator_with_params("deco_args")
def foo3():
    print 'hellol'
foo3()

