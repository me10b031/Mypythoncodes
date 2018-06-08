'''Define a class named American which has a static method called printNationality'''

class American(object):

    @staticmethod
    def printNationality():
        print ("aMERICAN")

Saketh = American()
Saketh.printNationality()
American.printNationality()