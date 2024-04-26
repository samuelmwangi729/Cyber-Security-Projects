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
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
file_hashes={}
new_hashes={}
class FileIntegrityChecker(FileSystemEventHandler):
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
class RealTimeScanner(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return 
        #Alert the user that the files have been modified
        if event.event_type == 'created':
            print(f"New file created {event.src_path}")
        elif event.event_type == 'modified':
            print(f"File modified: {event.src_path}")
        elif event.event_type == 'deleted':
            print(f"File deleted: {event.src_path}")
    def scanner(self,folder_to_scan):
        watch_init = RealTimeScanner()
        watcher = Observer()
        watcher.schedule(watch_init, folder_to_scan, recursive=True)
        watcher.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            watcher.stop()
        watcher.join()
        
if __name__ == '__main__':
    integrityChecker = FileIntegrityChecker()
    path_to_scan = input("\nEnter the directory path\n")
    time.sleep(1)
    print("Please wait ...\n")
    if not path_to_scan:
        path_to_scan="/home/p1rate/Desktop"
    integrityChecker.listContents(path_to_scan)
    print(f"\n Choose an Options \n =============================================\n 1. Display Hashes for files in {path_to_scan}\n 2. Monitor Directory {path_to_scan} \n 3. Exit\n")
    ch = int(input())
    if ch==1:
        #show hashes here 
        for item,value in file_hashes.items():
            print(f"The hash for the file {item} was {value}")
    elif ch==2:
        rts = RealTimeScanner()
        rts.scanner(path_to_scan) 
    else:
        print("[+] Exiting ......")
        exit()