'''Define a custom exception class which takes a string message as attribute.'''

class Error(object):
    def __init__(self,message):
        self.message = message
        