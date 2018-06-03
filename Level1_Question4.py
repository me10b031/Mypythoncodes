'''Write a program which accepts a sequence of comma-separated numbers from console
and generate a list and a tuple which contains every number.'''

a = input("Please enter the numbers separated by commas")
b = a.split(',')
print (b)
print (tuple(b))