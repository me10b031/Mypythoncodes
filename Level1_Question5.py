'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
'''


class getprint(object):
    def __init(self,string):
        self.string = ""

    def getstring(self):
        self.string = input("Give Me Something")

    def printstring(self):
        print(self.string.upper())

a = getprint()
a.getstring()
a.printstring()
