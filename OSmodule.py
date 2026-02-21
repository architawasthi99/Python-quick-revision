#GETTING THE LOCATION OF CURRENT DIRECTORY
import os
loc=os.getcwd()
print(loc)

#CHANGING CURRENT WORKING DIRECTORY
#import os
#def current_path():
#    print("current wokring folder before")
#    print(os.getcwd())
#    print()
#current_path()
#os.chdir("path")
#current_path()   

#CREATING NEW FOLDER

#if(os.path.exists("testfolder1"))
#os.mkdir("testfolder1")
#for i in range(0,100):
#    os.mkdir(f"testfolder/DAY{i+1}")
#to rename folder
#for i in range(0,100):
#    os.rename(f"testfolder1/DAY{i+1}",f"testfolder1/Tutorial{i+1}")

#if you want to create nested folders

#os.makedirs("parents/child/grandchild")

#to remove folder
#os.rmdir("testfolder")

#listing files and folders
#files=os.listdir()
#print(files)

#PATH HANDLING

#check file exist or not
if(os.path.exists("calculator.py")):
    print("yes")
else:
    print("no") 

#os.path.exixts(".....") for both files and folders
##os.path.isfile(".....") for  files 
# #os.path.isdir(".....") fo folders

import os

folder = "pyhton"
file = "calculator.py"

full_path = os.path.join(folder, file)

print(full_path)      

print(os.environ)