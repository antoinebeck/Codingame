## Nested loops from codingame "There is no spoon episode 1" puzzle
## https://www.codingame.com/training/medium/there-is-no-spoon-episode-1
## solution by Antoine BECK 03-17-2017
import sys
import math

width = int(input())  # (given)the number of cells on the X axis
height = int(input())  # (given)the number of cells on the Y axis
nodes = [input() for i in range(height)] #get every line of input
closest_x = -1
closest_y = -1

for y in range(height):
    for x in range(width): #For every potential node
        closest_x = -1
        closest_y = -1
        if nodes[y][x] == '0': #Node exists
            print(str(x) + ' ' + str(y), end=' ')
            
            for x2 in range(width-1, x, -1): #Closest right node(loop from end of line)
                if nodes[y][x2] == '0': 
                    closest_x = x2
                    
            if closest_x == -1: 
                print("-1 -1", end=' ')
            else: 
                print(str(closest_x) + ' ' + str(y), end=' ')
                
                
            for y3 in range(height-1, y, -1): #Closest bottom node(loop from end of column)
                if nodes[y3][x] == '0':
                    closest_y = y3
                    
            if closest_y == -1: 
                print("-1 -1")
            else: 
                print(str(x) + ' ' + str(closest_y))
