#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
from collections import Counter
def findDigits(n):
    c=0
    for x,y in Counter(str(n)).items():
        if int(x) and not n%int(x):
            c+=y
    return c

for _ in range(int(input())):
    print(findDigits(int(input())))
# Complete the findDigits function below.
# def findDigits(n):
#     num = [int(d) for d in str(n)]
#     count = 0
#     for i in num:
#         if(n%i==0):
#             count += 1
#     return count
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         n = int(input())

#         result = findDigits(n)

#         fptr.write(str(result) + '\n')

#     fptr.close()
