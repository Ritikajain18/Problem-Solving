'''
Given an array of integers, find and print the maximum number of integers you can select 
from the array such that the absolute difference between any two of the chosen integers is 
less than or equal to 1. For example, if your array is a=[1,1,2,2,4,4,5,5,5], you can create 
two subarrays meeting the criterion:[1,1,2,2] and [4,4,5,5,5]. The maximum length subarray 
has 5 elements.

Function Description

Complete the pickingNumbers function in the editor below. It should return an integer that 
represents the length of the longest array that can be created.

pickingNumbers has the following parameter(s):

a: an array of integers'''

import math
import os
import random
import re
import sys

# def pickingNumbers(a):
#     count = 0
#     # a.sort(reverse = True)
#     a.sort()
#     for i in range(len(a)-1):
#         if(abs(a[i]-a.get(i+1,0)<=1)):
#             count += 1
#     return count

from collections import Counter
def pickingNumbers(a):
    a = Counter(a)
    return max(a[k]+a.get(k+1,0) for k in sorted(a))
input()
a = map(int,input().split())
print(pickingNumbers(a))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     a = list(map(int, input().rstrip().split()))

#     result = pickingNumbers(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()
