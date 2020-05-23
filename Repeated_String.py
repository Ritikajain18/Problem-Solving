import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    sub_s = (s* (int(n/len(s))+1))[:n]
    count = 0
    for c in sub_s:
        if c =='a':
            count +=1
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

