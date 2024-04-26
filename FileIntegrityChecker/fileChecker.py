#!/usr/bin/python
'''
This project aims to check the integrity of all files in a given directory
This is done by checking their hashes after some time from a list of stored hashes
1. Ask for the directory from user
2. read the files in all the directories
3. generate their hashes ans store them in a dictionary
4. run watchdog to check if the file has been modified
'''
import os
import hashlib
import watchdog
import time
file_hashes={}
class FileIntegrityChecker():
    def __init__(self):
        self.Banner()
        print("\nLaunching the File Integrity Checker...")
        self.Banner()
    def Banner(self):
        for i in range(0,50):
            print("=",end="")
    '''list the directories '''
    def listContents(self,path=None):
        try:
            contents = os.listdir(path)
            #check if an item is a directory or file 
            for item in contents:
                if os.path.isdir(os.path.join(path,item)):
                    #if its  a directory, we list the files
                    self.listContents(os.path.join(path,item))
                else:
                    # generate the hashes 
                    self.GenerateHash(item,os.path.join(path,item))
        except:
            print("Sorry, The files Could not be read")
            return False
    def GenerateHash(self,filename,filepath):
        #generate the hash of the files, you can use sha128, sha256 etc
        #in this example, we use sha512
        #you can also use md5
        hasher = hashlib.sha512()
        #read the file to get their contents
        with open(filepath,'rb') as f:
            while True:
                data_chunk = f.read(4096)
                if not data_chunk:
                    break
                hasher.update(data_chunk)
        file_hashes[filename] = hasher.hexdigest()

if __name__ == '__main__':
    integrityChecker = FileIntegrityChecker()
    path_to_scan = input("\nEnter the directory path\n")
    if not path_to_scan:
        path_to_scan="/"
    integrityChecker.listContents(path_to_scan)
    for item,value in file_hashes.items():
        print(f"The hash for the file {item} is {value}")