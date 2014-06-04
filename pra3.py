def deco(func):
    print("before myfunc() called.")
    func()
    print("after myfunc() called.")
    return func
@deco  #the some as deco(myfunc)
def myfunc():
    print("myfunc() called.")

myfunc()
myfunc()
