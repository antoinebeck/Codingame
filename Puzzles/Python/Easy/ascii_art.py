## ASCII art string encoding from codingame "ASCII Art" puzzle
## https://www.codingame.com/training/easy/ascii-art
## solution by Antoine BECK 03-15-2017
import sys
import math

l = int(input()) # (given)WIDTH
h = int(input()) # (given)HEIGHT
t = input()      # (given)TEXT 
alphabet = [str(input()) for i in range(h)] # (given) Ascii font

num_txt = [ord(char) - 65 for char in t.upper()] #convertig text to array of numerical values a/A=0 z/Z=25

for i in range(h):
    for char in num_txt:
        if char > 25 or char < 0: ##Print '?'' if out of range
           char = 26 
        for j in range(l):
            print(alphabet[i][char * l + j], end="")        
    print("")
