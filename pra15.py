def decorator_whith_params_and_func_args(func):
        def handle_args(*args, **kwargs):
            print "begin" 
	    func(*args, **kwargs) 
	    print "end" 
	    print  func, args,kwargs
            return 'here have no arg_of_decorator' 
        return handle_args 

@decorator_whith_params_and_func_args
def foo4(a, b=2): 
    print "Content" 

print foo4(1, b=3)
