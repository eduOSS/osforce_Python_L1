def f(x):
    def f2(y):
	return x+y
    return f2

print f(5)(10)
#great
