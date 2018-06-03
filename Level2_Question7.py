'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
'''

a = int(input("please enter no of rows"))
b = int(input("please enter no of columns"))
l = []
m = []
for i in range (0,a):
    for j in range (0,b):
        c = i*j
        l.append(c)
    m.append(l)
    l = []

print (m)

