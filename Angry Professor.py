'''
Complete the angryProfessor function in the editor below. It must return YES if class 
is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):

k: the threshold number of students
a: an array of integers representing arrival times
'''

def angryProfessor(k, a):
    s = 0 
    for i in a:
        if i<1:
            s+=1
    return "YES" if s<k else "NO"

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = map(int,input().split())
    print(angryProfessor(k, a))


