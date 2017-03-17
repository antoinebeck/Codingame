## Distance formula and data parsing from codingame "Defibrillators" puzzle
## https://www.codingame.com/training/easy/defibrillators
## solution by Antoine BECK 03-15-2017
import sys
import math

lon = float(input().replace(',', '.')) # (given)User longitude
lat = float(input().replace(',', '.')) # (given)User latitude
n = int(input())# (given)number of defibrillators
defibs = []
count = 0
closest = 0
last_dist = 4000000.0

for i in range(n):
    defibs.append(input().split(';')) # 2D array of defibrillators
    
for defib in defibs:
    def_lon = float(defib[4].replace(',', '.'))
    def_lat = float(defib[5].replace(',', '.'))
    
    #Distance formula:
    x=(def_lon - lon) * math.cos((lat+def_lat)/2)
    y=def_lat - lat
    dist = math.sqrt(pow(x,2)+pow(y,2)) * 6371
    
    if(dist < last_dist): # Look for smallest distance
        last_dist = dist
        closest = count
    count+=1
    
print(defibs[closest][1])
