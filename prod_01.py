# calls in os library
import os

# this is to direct the python script to load files from the sub folder example_files
os.chdir('example_files')
# this grabs all files in that sub folder
filePath = os.listdir(os.getcwd())

# if striprtf package is not installed, perform this: pip3 install striprtf
#general knowledge on {\rtf1\ansi\...} --> reading 3 files contain this
#what i did was, i created a RTF file and copy, paste and rename to create the other 2 files (cei, txt)
from striprtf.striprtf import rtf_to_text

# How to copy files in Python? use shutil package
import shutil

#what you want to find in the files
toFind = input("Enter what you want to find: ")

#default to keyword = Robin
if len(toFind) < 1:
    toFind = "Robin"

for individualFile in filePath:
#these codes do not work with file types DS_Store, docx, xlsx, and pdf
    if not individualFile.endswith(("DS_Store","docx","xlsx","pdf")):
        try:
            with open(individualFile) as singleFile:
                #print(individualFile)  #debugging
                for line in singleFile.readlines():
                    #change rtf format to text format
                    rtfToText = rtf_to_text(line)
                    #rstrip() stripping all kinds of trailing whitespace by default
                    stripWhitespace = rtfToText.rstrip()
                    if stripWhitespace.find(toFind) == -1: continue
                    print("Found " + stripWhitespace + " in the file: " + individualFile)
                    # To copy files from "example_files" folder to "newFileFolderForProject" folder
                    shutil.copyfile(individualFile, "../newFileFolderForProject/"+individualFile)
        except OSError as error:
            print('error %s', error)

