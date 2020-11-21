#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
    s = [abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1)]
    return "Funny" if list(reversed(s))== s else "Not Funny"

for _ in range(int(input())):
    print(funnyString(input()))


