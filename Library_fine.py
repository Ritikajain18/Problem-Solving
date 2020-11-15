# #!/bin/python3
# 1 - returned 
# 2 - due
import math
import os
import random
import re
import sys

def libraryFine(d1,m1,y1,d2,m2,y2):
    if y1>y2:
        #if year of return is greater than year due
        return 10000
    elif m1>m2 and y1==y2:
        #if returned in the same year and month of return is greater than month due
        return (m1-m2)*500
    elif d1>d2 and y1==y2 and m1==m2:
        #if returned in the same year and month, and the date of return is greater than due date
        return (d1-d2)*15
    else:
        return 0

d1,m1,y1 = map(int,input().split())
d2,m2,y2 = map(int,input().split())
print(libraryFine(d1,m1,y1,d2,m2,y2))
