import sys

s = input().strip()
n=1
for l in s:
    if l.isupper():
        n+=1
print (n)

