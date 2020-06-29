'''
You are given an array of n integers and a positive integer,k . Find and print the 
number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k .

For example,ar=[1,2,3,4,5,6] and k=5. Our three pairs meeting the criteria are[1,4],[2,3] and [4,6].

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer 
count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

n: the integer length of array ar
ar: an array of integers
k: the integer to divide the pair sum by'''


import math
import os
import random
import re
import sys

n, k = map(int,raw_input().split())
arr = map(int,raw_input().split())
count = 0
for i in range(0, n):
    for j in range(i+1, n):
        if (arr[i] + arr[j]) % k == 0:
            count += 1
print count
