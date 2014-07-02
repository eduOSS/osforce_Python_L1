#!usr/bin/python
#!coding:utf8
def isDuplicate(s):
    s2 = ''.join(set(s))
    if len(s2) < len(s):
        return False
    else:
	return True
i = isDuplicate
print i("helo i am ")    
#this function says that if there are multiple ' ' in the string it returns "False"
print i("hello")
#this function says that if there are non-space character in the string it returns also "False"
print i("helo") 
#here it print True
    
