## ASCII to unary from codigame "Chuck Norris" puzzle
## https://www.codingame.com/training/easy/chuck-norris
## solution by Antoine BECK 03-15-2017
import sys
import math

message = input() #input provided
char_count = 0    #used to count the chars in input
current_bit = ';' #current bit initialised to random not-a-bit character
    
for char in message:
    binary_char = str(bin(ord(char))[2:].zfill(7)) #Convert char into string of the 7bits
    
    for bit in binary_char :
        if bit != current_bit: #Begin a new serie
            if current_bit !=  ';': #End previous serie (if not first)
                print(' ', end='')
                
            if bit == '0': #New bit
                print("00 0", end='')#one 0
            else:
                print("0 0", end='') #one 1

            current_bit = bit #update current bit
        else:
            print('0', end='') #Continuation of a serie
            
    char_count +=1
