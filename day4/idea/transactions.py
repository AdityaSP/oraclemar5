
# ac = bank.Account('Aditya', 10000, 'S')
# print ac.n, ac.b, ac.t
# print ac
# ac.credit(1000000)
# ac.debit(100)
# print ac.b
#
# ac1 = bank.Account('Arun')
# print ac1.n, ac1.b, ac1.t
# print ac1
# ac1.credit(1000)
# ac1.debit(5000)
# print ac1.b

import bank
sa = bank.SA('Aditya', 1000, 'S')

if sa.b > 2000:
    sa.debit(2000)

ca = bank.CA('ABC Pvt Ltd', 0, 'C')
ca.debit(1000)
print "Balance of SA" , sa.b
print "Balance of CA", ca.b