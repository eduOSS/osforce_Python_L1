import thread
import threading
import time

def runnable():
    while 1:
        print 'world cup'
        time.sleep(1)

thread.start_new_thread(runnable,())

while 1:
    time.sleep(10)
