#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    tot = sum(arr)
    add = 0
    for i in arr:
        if(add == tot-i-add):
            return 'YES'
        add += i
    return 'NO'

for _ in range(int(input())):
    input()
    arr = list(map(int,input().split()))
    print(balancedSums(arr))
    

