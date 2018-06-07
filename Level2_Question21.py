'''A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position
after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2'''

import math
list = []
while True:
    l = input()
    if not l:
        break
    list.append(l.split(' '))
y = int(list[0][1]) - int(list[1][1])
x = int(list[2][1])- int(list[3][1])

d = math.sqrt((abs(y)**2+abs(x)**2))
print (round(d))

