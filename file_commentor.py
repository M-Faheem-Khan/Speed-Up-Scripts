# Author: Muhammad F. Khan
# FileName: file_commenter.py
# Description: Adds comments to (JAVA + C) files
# License: MIT

'''
How to use?
run the program using python3 # -> python3 file_commenter.py
Fill in the requested information
AuthorName, Version, Description, Absolute Path to your source file.
'''

# IMPORTS
import os
from datetime import datetime

# VARIABLES
now = datetime.now() # current date time
# GETTING AUTHOR + PROGRAM INFO
AuthorName = input("Author Name: ")
ProgramVersion = input("Version: ")
ProgramDescription = input("Program Description: ")
numberOfFiles = 0 # number of files comments added to

# Adds Comments to All Source files
src_dir = input("Source Folder(Absolute Path): ")

# GETTING FILES IN DIRECTORY
files = os.listdir(src_dir)

# ITTERATING OVER FILES + ADDING COMMENTS
for file in files:
    content = None
    fname = file
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S") # getting formatted datetime
    # creating formatted comment string
    formattedComment = "/*\n* Name: %s\n* Version: %s\n* FileName: %s\n* Timestamp(date comments added): %s\n* Description: %s\n*/\n" % (AuthorName, ProgramVersion, file, date_time, ProgramDescription)
    with open(os.path.join(src_dir, file), "r+") as f:
        content = formattedComment + "\n" + f.read()

    # ADD COMMENTS TO THE TOP OF THE FILE
    with open(os.path.join(src_dir, file), "w") as f:
        f.write(content)
        numberOfFiles++ # incrementing number of files

print("Comment Add to %d files" % numberOfFiles)
