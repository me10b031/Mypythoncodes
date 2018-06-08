'''Define a class named American and its subclass NewYorker.'''

class American(object):
    age = 20
    def __init__(self,name):
        self.name = name
class NewYorker(American):
    def __init__(self,age):
        self.age = age

saketh = American("hero")
barath = NewYorker(10)
print (saketh.age)
print (barath.age)

