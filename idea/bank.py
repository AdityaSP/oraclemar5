class Account(object):
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t

    def credit(self, amount):
        self.b += amount

    def debit(self, amount):
        self.b -= amount

class SA(Account):

    def debit(self, amount):
        if self.b > amount:
            self.b -= amount
        else:
            raise ValueError("Insufficient Balance")

class CA(Account):
    pass
