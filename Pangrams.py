import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = set(s)
    s.discard(" ")
    return "pangram" if len(s)==26 else "not pangram"
print(pangrams(input().lower()))