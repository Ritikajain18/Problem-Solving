'''Watson likes to challenge Sherlock's math ability. He will provide a starting 
and ending value describing a range of integers. Sherlock must determine the number 
of square integers within that range, inclusive of the endpoints.

Complete the squares function in the editor below. It should return an integer 
representing the number of square integers in the inclusive range from a to b.

squares has the following parameter(s):

a: an integer, the lower range boundary
b: an integer, the uppere range boundary
'''

from math import sqrt

def squares(a, b):
    c = int(sqrt(b))-int(sqrt(a))
    return c+1 if int(sqrt(a))**2==a else c

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(squares(a, b))

