import os,os.path
import glob
path=r'C:\Users\ronni\OneDrive\Documents'
zero = [ f.path for f in os.scandir(path) if f.is_dir() ]
print(zero)
##this above gives the list of all the folders in the given folder
##gives the folders that are empty
lists=[[]]*len(zero)
for i in range(0,len(zero)):
    arr=glob.glob((zero[i])+"\*")
    lists[i]=sorted(arr)
    lists[i].sort(key=len)
    if (len(lists[i]))<1:
        print(zero[i],i)
    else:
        continue