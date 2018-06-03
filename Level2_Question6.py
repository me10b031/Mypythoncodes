'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.'''

import math
C = 50
H = 30
D = input("Please Enter the numbers separated by commas")
l = D.split(",")
print (l)
m = []
for i in l:
    Q = math.sqrt((2*C*float(i))/H)
    m.append(str(round(Q)))

print (','.join(m))

