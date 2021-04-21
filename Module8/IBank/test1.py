import unittest

from iBank_menu import Account, CreditAccount


class TestAccount(unittest.TestCase):
    def test_create_account(self):
        account = Account('Иван', '12345678', 90000000000, start_balance=1000)
        self.assertEqual(account.name, 'Иван')
        self.assertEqual(account.passport8, '12345678')
        self.assertEqual(account.balance, 1000)

    def test_deposit(self):
        account = Account('Иван', '12345678', 90000000000)
        self.assertEqual(account.balance, 0)