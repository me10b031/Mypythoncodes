'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''

a = input("Please input the digit")
b = int(a)

p = b
q = 10*b + p
r = 100*b + q
s = 1000*b + r

print (p+q+r+s)