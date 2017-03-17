## Closest value to zero from codingame "Temperatures" puzzle
## https://www.codingame.com/training/easy/temperatures
## solution by Antoine BECK 03-15-2017
## Note: a positive value has priority over a negative value (n is a better output than -n)
import sys
import math

n = int(input()) # (given) the number of temperatures to analyse
temps = input()  # (given) the n temperatures expressed as integers ranging from -273 to 5526
closest = 5526	 # closest to zero temp found, initialised to max range

if n==0: #Empty array check
    print(0)
else:
    values = map(int, temps.split(' ')) #Mapping values to int
    for value in values:
        if abs(closest) - abs(value) > 0 or (abs(closest) == abs(value) and value > closest):
            closest = value
    print(closest)
