'''
Function Description

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the 
bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes 
Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill

'''

def bonAppetit(bill, k, b):
    return b-(sum(bill)//2-bill[k]//2) or "Bon Appetit"
n,k = map(int,input().split())
bill = list(map(int,input().split()))
b = int(input())
print(bonAppetit(bill, k, b))
