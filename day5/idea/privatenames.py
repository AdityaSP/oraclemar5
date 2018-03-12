class Shape(object):

    def __init__(self):
        self.__name = 'Circle'

    def get_name(self):
        self.__sayhi()
        return self.__name

    def __sayhi(self):
        print "Hi"
    def _greet(self):
        print "Hello"

circle = Shape()
#print circle.__name
print circle.get_name()
#circle.__sayhi()
#circle._greet()