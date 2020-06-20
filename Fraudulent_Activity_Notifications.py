'''HackerLand National Bank has a simple policy for warning clients about possible fraudulent 
account activity. If the amount spent by a client on a particular day is greater than or
equal to  the client's median spending for a trailing number of days, they send the client
a notification about potential fraud. The bank doesn't send the client any notifications 
until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of 
days, find and print the number of times the client will receive a notification over all  
days.
Complete the function activityNotifications in the editor below. It must return an 
integer representing the number of client notifications.

activityNotifications has the following parameter(s):

expenditure: an array of integers representing daily expenditures
d: an integer, the lookback days for median spending'''

import math
import os
import random
import re
import sys
import statistics 
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notify = 0
    lead = expenditure[d+1:]
    for i in range(len(lead)):
        med = statistics.median(expenditure[i:d+1])
        if(lead[i]>=med):
            notify += 1
    return notify

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()


