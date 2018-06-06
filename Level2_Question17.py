'''Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''
D = 0
W = 0
content = []
while True:
    line = input()
    if line:
        content.append(line.upper())
    else:
        break
for line in content:
    if line[0] == 'D':
        D = D + int((line[2:]))
    if line[0] == 'W':
        W = W + int(line[2:])


print (D-W)
