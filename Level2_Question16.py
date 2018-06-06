'''Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9'''

a  = input("Please enter numbers separated by commas")
c = a.split(',')
print (c)
list = []
for i in c:
    b = int(i)
    if b%2 != 0 :
        if i not in list:
            list.append(i)
print (','.join(list))
