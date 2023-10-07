#! /usr/bin/python3

import os

#first get all the content of the present working directory including files and directory
dirContent = os.listdir(os.getcwd())

#create a two list, one for files, the other for directories.
directories = []
files = []

#create a function that loops through the content of the the current directory, identifies the files and directories and appends it to the suitable list
def sorter():
    #using for loop to loop through dirContent
    for content in dirContent:
        #using conditionals to check for type of content and then append to the respective list
        if os.path.isdir(os.path.join(os.getcwd(), content)):
            directories.append(content)
        elif os.path.isfile(os.path.join(os.getcwd(), content)):
            files.append(content)
#a function to check if there's no file or directory in the current directory. This will use conditionals to either print the directories and files or print no direcories or files, or which ever condition is true.
def printer():
    if len(directories) != 0 and len(files) != 0:
        if len(directories) == 1:
            print("This directory contains 1 directory. The directory is:")
            print(directories)
        else:
            print("This directory contains " + str(len(directories)) + " directories. The directories are:")
            print(directories)

        print("\n")

        if len(files) == 1:
            print("This directory contains 1 file. The file is:")
            print(files)
        else:
            print("This directory contains " + str(len(files)) + " files. They files are:")
            print(files)

    elif len(directories) != 0 and len(files) == 0:
        print("This directory contains 0 file.\n")

        if len(directories) == 1:
            print("This directory contains 1 directory. The directory is:")
            print(directories)
        else:
            print("This directory contains " + str(len(directories)) + " directories. The directories are:")
            print(directories) 
 
    elif len(directories) == 0 and len(files) != 0:
        print("This directory contains 0 directory.\n")
        
        if len(files) == 1:
            print("This directory contains 1 file. The file is:")
            print(files)
        else:
            print("This directory contains " + str(len(files)) + " files. They files are:")
            print(files)
 
    elif len(directories) == 0 and len(files) == 0:
        print("This directory is empty")

sorter()
printer()
#print(directories)
#print(files)
