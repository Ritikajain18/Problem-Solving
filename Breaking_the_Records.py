'''
Maria plays college basketball and wants to go pro. Each season she maintains a record 
of her play. She tabulates the number of times she breaks her season record for most points
and least points in a game. Points scored in the first game establish her record for the 
season, and she begins counting from there.

For example, assume her scores for the season are represented in the array scores = [12,24,10,24].
Scores are in the same order as the games played. She would tabulate her results as follows:

                                 Count
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1
Given Maria's scores for a season, find and print the number of times she breaks her 
records for most and least points scored during the season.


Function Description

Complete the breakingRecords function in the editor below. It must return an integer array 
containing the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.

breakingRecords has the following parameter(s):

scores: an array of integers'''


import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    highest_record = 0
    lowest_record = 0
    for i in scores:
        if(i< max_score):
            max_score = i
            highest_record += 1
        if(i> min_score):
            min_score = i
            lowest_record += 1
    return (lowest_record, highest_record)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


