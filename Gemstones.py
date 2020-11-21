#!/bin/python3

import math
import os
import random
import re
import sys

rocks = [set(input()) for _ in range(int(input()))]
gems = set.intersection(*rocks)
print(len(gems))
# Complete the gemstones function below.
