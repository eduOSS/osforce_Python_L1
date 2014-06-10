def decorator_whith_params_and_func_args(arg_of_decorator):
    def handle_func(func):
        #def handle_args(*args, **kwargs):
            print "begin" 
	    func() 
	    print "end" 
	    print arg_of_decorator, func#, args,kwargs
            return func 
	#return handle_args 
    return handle_func 

@decorator_whith_params_and_func_args("123") 
def foo4():
    print "Content" 

print foo4()#(1, b=3)
