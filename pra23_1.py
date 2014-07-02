import sys
_back = sys.stdout
f = open("leo.txt","w")
sys.stdout = f
print "haha"
print sys.platform
f.close()
