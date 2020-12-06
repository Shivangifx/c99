import os
import shutil



source = input("Pls enter the source: ")
dest = input("Pls enter the destination: ")
sorce = source+'/'
dest = dest+'/'
lof = os.listdir(sorce)

for file in lof:
    shutil.copy(sorce+file,dest)

   
