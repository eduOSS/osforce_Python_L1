import shutil
import re
import os

dir = '/home/leo/Documents/python/osforce/'

if os.path.isdir(dir):
    print 'directory exists'
else: 
    print 'directory not exists'
    time.sleep(5)
    exit()

filelist=[]
filelist = os.listdir(dir)
for i in filelist:
    if i[0:4] == 'exce':
	NewName = 'exer'+i[4:]
        shutil.move(dir+i,dir+NewName)
