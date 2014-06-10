def decorator_whith_params_and_func_args(func): #(arg_of_decorator)
    #def handle_func(func):
        def handle_args(*args, **kwargs):
            print "begin" 
	    func(*args, **kwargs) 
	    print "end" 
	    print  func, args,kwargs
            return 'here have no args' 
	return handle_args 
    #return handle_func

@decorator_whith_params_and_func_args#("123")
def foo4(a, b=2): 
    print "Content" 

print foo4(1, b=3)
