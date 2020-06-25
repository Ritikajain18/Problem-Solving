'''
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
In the diagram below, the red region denotes his house, where s is the start point, and t
is the endpoint. The apple tree is to the left of his house, and the orange tree is to its 
right. You can assume the trees are located on a single point, where the apple tree is at 
point a, and the orange tree is at point b.

When a fruit falls from its tree, it lands d units of distance from its tree of origin 
along the x-axis. A negative value of d means the fruit fell d units to the tree's left, 
and a positive value of d means it falls d units to the tree's right.

Given the value of d for m apples and n oranges, determine how many apples and oranges 
will fall on Sam's house (i.e., in the inclusive range[s,t] )?

Function Description

Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.'''

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(s <= a + d <= t for d in apples))
    print(sum(s <= b + d <= t for d in oranges))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

