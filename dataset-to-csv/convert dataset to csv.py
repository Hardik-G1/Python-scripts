from PIL import Image
import csv
import os
subdirs = [x[0] for x in os.walk('Training image')]
data=[]
with open('imags11.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    for i in range(1,len(subdirs)):
        for filename in os.listdir(subdirs[i]):
            data.append([filename,subdirs[i]])
            writer.writerow([filename, subdirs[i][15:]])

            data=[]
writeFile.close()
