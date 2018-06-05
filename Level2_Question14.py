'''Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

UPPER = 0
LOWER = 0
import string
a = input("Please Enter Something")
for m in a:
    if m in list(string.ascii_lowercase):
        LOWER = LOWER + 1
    if m in list(string.ascii_uppercase):
        UPPER = UPPER + 1

print('UPPER CASE {0}'.format(UPPER))
print('LOWER CASE {0}'.format(LOWER))