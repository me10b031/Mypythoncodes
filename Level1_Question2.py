'''program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program'''

a = int(input("please enter a number"))
b = 1
for i in range (1,a+1):
    b = b * i

print (b)