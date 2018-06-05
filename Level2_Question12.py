'''Write a program, which will find all such numbers between 1000 and 3000 (both included) such that
each digit of the number is an even number.'''

list = []
for i in range (1000,3001):

    n =  str(i)
    if int(n[0])%2 == 0 and int(n[1]) % 2 == 0 and int(n[2])%2 == 0 and int(n[3])%2 == 0:
            list.append(i)
print (list)


