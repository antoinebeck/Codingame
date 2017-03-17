## Array optimisation from codingame "Horse Racing Duals" puzzle
## https://www.codingame.com/training/easy/horse-racing-duals
## solution by Antoine BECK 03-15-2017
import sys
import math

n = int(input())
pi = []
diff = 10000000
tmp = 0
for i in range(n):
    pi.append(int(input()))

pi.sort() # Using the sort function (optimized)

for i in range(n-1):
    tmp = pi[i+1] - pi[i]
    if  tmp < diff:
        diff = tmp
    if diff == 0:
        break
print(diff)