'''
Dan is playing a video game in which his character competes in a hurdle race. Hurdles are of varying heights, and Dan has a maximum height he can jump. There is a magic potion he can take that will increase his maximum height by  unit for each dose. How many doses of the potion must he take to be able to jump all of the hurdles.

Given an array of hurdle heights height, and an initial maximum height Dan can jump,k, 
determine the minimum number of doses Dan must take to be able to clear all the hurdles in 
the race.

For example, if height =[1,2,3,3,2] and Dan can jump 1 unit high naturally, he must take 
3-1=2 doses of potion to be able to jump all of the hurdles.
Complete the hurdleRace function in the editor below. It should return the minimum 
units of potion Dan needs to drink to jump all of the hurdles.

hurdleRace has the following parameter(s):

k: an integer denoting the height Dan can jump naturally
height: an array of integers denoting the heights of each hurdle
'''
import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_height = max(height)
    if(k>=max_height):
        return ('0')
    else:
        return(max_height-k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()


