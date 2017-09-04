import sys
sys.stdout=open("test.txt","w")
print ("hello")
sys.stdout.close()