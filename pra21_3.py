#!/usr/bin/python
#coding:utf8

__author__ = ['leo']

import thread,threading,time

lock = threading.Lock()

class A(threading.Thread):
    def run(self):
	start = time.time()
        while time.time() - start < 5:
            time.sleep(0.01)
	    print 'world cup AAA'

class B(threading.Thread):
    def run(self):
	start = time.time()
        while time.time() - start < 5:
            time.sleep(0.01)
	    print 'world cup BBB'

a = A()
b = B()
a.start()
b.start()
b.join()
a.join()
