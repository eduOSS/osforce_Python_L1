#!/usr/bin/python
#coding:utf8

import multiprocessing
import time

class P(multiprocessing.Process):
    def run(self):
        while 1:
	    time.sleep(1)
	    print 'world cup'

subprocess_list = []

for i in range(10):
    subprocess_list.append(P())

for p in subprocess_list:
    p.start()

for p in subprocess_list:
    p.join()
