class A(object):
    '''
	doc
    '''
    name = 'A'
    
    def __init__(self,_id):
	self.id = _id
	print 'A'
	'''
	    docs
	'''
    def msg(self):
	print 'msg'

print dir(A)
print 'A.__dict_',A.__dict__
print 'A.__delattr_',A.__delattr__
print 'A.__doc_',A.__doc__
