import unittest
import bank
import HtmlTestRunner

class TestBank(unittest.TestCase):
    def test_addition(self):
        a = 3 + 7
        assert a == 10, 'Was expecting 10'

    def test_sub(self):
        a = 3 - 7
        assert a == -4, 'Was expecting 10'

    def test_SA(self):
        sa = bank.SA('Aditya',1000,'S')
        assert sa.b == 1000, 'Was expecting the balance to be 1000'

    def test_debitSA(self):
        sa = bank.SA('Aditya', 1000, 'S')
        sa.debit(300)
        assert sa.b == 700, 'Was expecting the balance to be 700'

    def test_insufficient(self):
        sa = bank.SA('Aditya', 10, 'S')
        try:
            sa.debit(100)
        except ValueError as err:
            assert err.message == 'Insufficient Balance'

#unittest.main(verbosity = 3)
suite = unittest.TestSuite()
suite.addTest(TestBank('test_debitSA'))
suite.addTest(TestBank('test_insufficient'))

#runner = unittest.TextTestRunner(verbosity=3)
#runner.run(suite)
runner = HtmlTestRunner.HTMLTestRunner(output="reports")
runner.run(suite)