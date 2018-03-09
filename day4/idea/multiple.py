class A(object):
    def f1(self):
        print "from A"

class B(A):
    pass

class C(A):
    def f1(self):
        print "from C"

class D(B,C):
    pass


#Linearization of Multi-derived Classes
#mro = Method Resolution Order
print D.__mro__
objd = D()
objd.f1()