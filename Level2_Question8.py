'''Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.'''

a = input("Enter a list of words separated by comma to be sorted ")
b = a.split(',')
b.sort()
print (','.join(b))