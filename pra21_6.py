#!/usr/bin/python
#coding:utf8

import time,multiprocessing
queue = multiprocessing.Queue()

class comsumer(multiprocessing.Process):
    def run(self):
	while 1:
	    time.sleep(1)
  	    msg = queue.get()
	    if msg:
	        print msg

class producer(multiprocessing.Process):
    def run(self):
	while 1:
	    time.sleep(2)
	    stime = str(time.time())
            msg = 'the time is '+stime
	    queue.put(msg)

c = comsumer()
p = producer()

c.start() 
p.start() 

c.join()
p.join()
