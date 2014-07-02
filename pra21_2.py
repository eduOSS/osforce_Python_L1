import thread,threading,time

class T(threading.Thread):
    def run(self):
	start = time.time()
        while time.time() - start < 5:
            time.sleep(1)
	    print 'world cup'

t = T()
t.start()
print t.isAlive()
t.join()
print t.isAlive()
