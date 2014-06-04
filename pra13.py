def res(ls1,ls2,repl):
    l1 = len(ls1)
    l2 = len(ls2)
    i = 0
    res = []
    while i < l1 and i < l2:
	res.append((ls1[i],ls2[i]))
	i  = i + 1
    while i < l1:
	res.append((ls1[i],repl))
	i  = i + 1
    while i < l2:
	e(repl,ls2[i]))
	i  = i + 1
    return res
print res([1,2,4,5,7,],[23,4,5,7,87,34,12],'r')
