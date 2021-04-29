#!/usr/bin/env python3
import os, glob
import time
# import report
from shutil import copyfile
from shutil import copymode
from shutil import copytree
from shutil import rmtree

#src = "D:\\New folder\\20200822"
src = "D:\\_Backup\\_PPPFilesBackup"
dest = "D:\\_Backup\\_PPPAllPhotos"
#folder = "CSVsBackupFeb21"
#dest = "_temp2"

created_file = "report/report3.pdf"



def create_path(path, name, extension, version):  
    """ Returns a joined path """
    filename = name + "_"+str(version) + extension
    return os.path.join(path, filename)

def is_file_empty(filename):
    """ Check if file is empty by reading first character in it """
    with open(filename, 'r') as file:
        first_char = file.read(1)
        if not first_char:
            return True
    return False

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "It took %d:%02d:%02d" % (hour, minutes, seconds)


def search_and_copy_files(source,folder_to):
    message = ""
    count = 0
    list = []
    for subdir, dirs, files in os.walk(source):
        for folder in os.listdir(subdir):
            if folder == "Pictures" or folder == "pictures":
                picsFolder = os.path.join(subdir,folder)
                if os.path.isdir(picsFolder):
                    for item in os.listdir(picsFolder):
                        itemPath = os.path.join(picsFolder,item)
                        newItem = os.path.join(dest, item)
                        if not os.path.exists(newItem):
                            try:
                                copytree(itemPath,newItem)
                                count = count + 1
                                print(newItem + " Successfuly copied")
                            except Exception as e:
                                print("Error occured while creating and copying files to "+newItem)

                        elif os.path.exists(newItem):
                            try:
                                rmtree(newItem)
                                print("Old files deleted")
                                copytree(itemPath,newItem)
                                count = count + 1
                                print(newItem + " copied!")
                            except OSError as e:
                                print("Error: %s : %s" % (newItem, e.strerror))
    return count
                    

if __name__ == "__main__":
    startTime = time.time()
    print(str(search_and_copy_files(src, dest)) + " files copied!")
    executionTime = (time.time() - startTime)
    print(convert(executionTime))
