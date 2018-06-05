'''Write a program that accepts a sentence and calculate the number of letters and digits.'''

Letters = 0
Digits = 0
import string
input = input("Please Enter Something")

a = str(input)

for m in a:
    if m in list(string.ascii_lowercase):
        Letters = Letters + 1

    if str(m) in ['0','1','2','3','4','5','6','7','8','9']:
        Digits = Digits + 1

print('LETTERS {0}'.format(Letters))
print('DIGITS {0}'.format(Digits))