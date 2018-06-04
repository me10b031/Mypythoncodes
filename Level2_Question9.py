'''Write a program that accepts sequence of lines as input and
prints the lines after making all characters in the sentence capitalized.'''

content = []
while True:
    line = input()
    if line:
        content.append(line.upper())
    else:
        break
for line in content:
    print (line)