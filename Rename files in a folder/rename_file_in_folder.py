import os
import os,os.path
import glob
os.chdir('C:\\Users\\i\\path where your files are')
i=0
dir = sorted(os.listdir(os.getcwd()), key=len)
for file in dir:
	src=file
	dst=str(i)+".jpeg"
	os.rename(src,dst)
	i+=1

