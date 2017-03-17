## Dictionary mim-type from filename from codingame "Mime type" puzzle
## https://www.codingame.com/training/easy/mime-type
## solution by Antoine BECK 03-15-2017
import sys
import math

n = int(input())  # (given) Number of elements which make up the association table.
q = int(input())  # (given) Number Q of file names to be analyzed.
ext_type_table={} # dictionary of mime extensions
fname = [] # filenames to process

for i in range(n):
    ext, mt = input().split() # (given) input
    ext_type_table[ext.lower()] = mt # Build table (extensions in lowercase)
for i in range(q):
    fname.append(input().lower())  #Array of file names (in lowercase)

for name in fname:
    name = name.split('.') #List all string separated by dots
    extension = name[len(name)-1]#Last string after dot (in case of Helo.test.txt)
    if len(name) < 2: #No '.' in filename
        print("UNKNOWN")
    elif extension in ext_type_table: #We have a type for that extension
        print(ext_type_table[extension])
    else:
        print("UNKNOWN")