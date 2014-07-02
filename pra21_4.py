#!/usr/bin/python
#coding:utf8

__author__ = ['leo']

import thread,threading,time

lock = threading.Lock()

class A(threading.Thread):
    def run(self):
	while True:
	    lock.acquire()
	    try:
		print 'aaa'
		time.sleep(0.1)
	    finally:
		lock.release()

class B(threading.Thread):
    def run(self):
	while True:
	    lock.acquire()
	    try:
		print 'bbb'
		time.sleep(0.1)
	    finally:
		lock.release()
a = A()
b = B()
a.start()
b.start()
b.join()
a.join()
