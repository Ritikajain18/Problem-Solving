'''
Consider a staircase of size n :

   #
  ##
 ###
####
Observe that its base and height are both equal to n, and the image is
drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n .'''

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1, n+1): print(str('#' * i).rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)

