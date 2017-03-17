## Vertical speed managment in simulation from codingame "Mars Lander 1" puzzle
## https://www.codingame.com/training/easy/mars-lander-episode-1
## solution by Antoine BECK 03-15-2017
## Note: aiming at best fuel efficiency
import sys
import math

##<Given> surface of mars
surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
##</Given>

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]# Given input
    power = 2 #Default mid-power
    
    if v_speed < -30: #EMERGENCY BOOST!
        power = 4  
    elif v_speed < -20 and power < 3: # Power back to safezone
        power += 1
    elif v_speed > -15 and power > 1: # In safezone, save fuel
        power -= 1
    print("0 " + str(power))
