# Author: Muhammad F. Khan
# Date: November 11, 2020
# Description: Generates hashes for files in current directory

import os, sys # for args and getting files in cwd
import hashlib # for generating hashes for files

FILE_BUFFER_SIZE = 65536 # 64KB file read buffer

# Color Codes for printing colored text
class Colors:
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# Gets all files in the current directories
def GetFiles():
    files = list() # list of files to generate hashes for
    # Removing directories, cache, hidden files
    for f in os.listdir(os.getcwd()):
        if not f.startswith('.') and not f.startswith('_'):
            if not os.path.isdir(f):
                files.append(f)
    return files # returning files in current directory


# Generates Hashes for a given file
def GenerateHashes(files):
    for fname in files:
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()

        with open(fname, 'rb') as f:
            while True:
                data = f.read(FILE_BUFFER_SIZE)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
        
        # Saving hashes to file
        SaveToFile(fname, md5.hexdigest(), sha1.hexdigest())

# Saves Hashes to a given file
def SaveToFile(fname, md5, sha1):
    # if the file does not exists create the file
    if not os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "w+") as f:
            f.write(f"File: {fname}\n")
            f.write(f"MD5: {md5}\n")
            f.write(f"SHA1: {sha1}\n")
    else:
        with open(sys.argv[1], "a") as f:
            f.write(f"File: {fname}\n")
            f.write(f"MD5: {md5}\n")
            f.write(f"SHA1: {sha1}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Colors.FAIL}Error: Missing Save File Parameter!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Example: {sys.argv[0]} hashes.txt{Colors.ENDC}")
        sys.exit(-1) # exit with error
    
    files = GetFiles()
    GenerateHashes(files)
