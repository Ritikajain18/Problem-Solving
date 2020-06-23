'''
Complete the miniMaxSum function in the editor below. 
It should print two space-separated integers on one line:
the minimum sum and the maximum sum of 4 of 5 elements.'''

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    x = sum(arr)
    print ((x-(max(arr))), (x-(min(arr))))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


