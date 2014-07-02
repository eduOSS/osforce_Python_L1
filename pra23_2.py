import subprocess,sys
process = subprocess.Popen("ls", shell = True)
stdout,stderr = process.communicate()
process.communicate()
_back=sys.stdout
sys.stdout = open("adams.txt","w")
print stdout,stderr
process1 = subprocess.Popen("cat adams.txt",shell=True)
stdout1,stderr1 = process.communicate()
sys.stdout=_back
print stdout1
print stdout
