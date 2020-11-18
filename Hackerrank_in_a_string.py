#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
# import re
for _ in range(int(input().strip())):
    print('YES' if re.search(r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*',input().strip()) else 'NO')

