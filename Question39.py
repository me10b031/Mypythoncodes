'''Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).'''

'''n = int(input())
a = 1

for i in range(1,n+1):
    a = a+100

print (a)'''

def f(n):
    if n==0:
        return 1
    else:
        return f(n-1)+100

n=int(input())
print (f(n))