# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from collections import Counter

def cutTheSticks(arr):
    arr.sort()
    prev = -1
    l = len(arr)
    for i in arr:
        if i!=prev:
            print(l)
        l-=1
        prev=i
input()
arr = list(map(int,input().split()))
cutTheSticks(arr)

