
"""program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line"""



list = []
for item in range (2000,3201):
    if item % 7 == 0 and item % 5 != 0:
        list.append(item)
print (str(list)[1:-1])


