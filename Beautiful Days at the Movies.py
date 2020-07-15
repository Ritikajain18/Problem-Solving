'''
Complete the beautifulDays function in the editor below. It must return the number of 
beautiful days in the range.

beautifulDays has the following parameter(s):

i: the starting day number
j: the ending day number
k: the divisor
'''


import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
# i,j,k = [int(num) for num in input().split()]
# count = 0
# for num in range(i,j+1):
#     if(num-int(str(num)[::-1]) % k==0):
#         count += 1
# print(count)

i,j,k = [int(x) for x in input().split()]
count = 0
for x in range(i,j+1):
    if (x - int(str(x)[::-1])) % k == 0:
        count += 1
print(count)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ijk = input().split()

#     i = int(ijk[0])

#     j = int(ijk[1])

#     k = int(ijk[2])

#     result = beautifulDays(i, j, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()


