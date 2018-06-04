'''Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.'''


a = input()
l = []
b = a.split()
for i in b:
    if i not in l:
        l.append((i))
l.sort()
print (' '.join(l))

