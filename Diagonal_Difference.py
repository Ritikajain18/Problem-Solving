'''Given a square matrix, calculate the absolute difference between the sums of its diagonals'''

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    primary = 0
    secondary = 0
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                primary += arr[i][j]
            if(i ==(n-j-1)):
                secondary += arr[i][j]
    return (abs(primary - secondary))
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
