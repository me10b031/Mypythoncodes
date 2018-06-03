'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the dictionary'''


a = int(input("please enter the number"))
dict = {}
for i in range (1,a+1):
    dict[i]= i*i

print (dict)
