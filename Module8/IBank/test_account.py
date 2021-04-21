import unittest
from iBank_menu import Account, CreditAccount, ACCOUNTS



# FIXME: Допишите тест/тесты, который выявит недоработки в классе Account ,
#  затем исправьте недоработки класса, чтобы тест проходил
class TestAccount(unittest.TestCase):
    def setUp(self):
        self.accounts = [Account("Петр", 12345678, "+79006001020", start_balance=300),
                         Account("Иван", 12345676, "+79006001020", start_balance=100)]

    def test_deposit(self):
        self.accounts[0].deposit(500)
        self.assertEqual(self.accounts[0].balance, 800)

    def test_withdraw(self):
        self.accounts[0].withdraw(200)
        self.assertEqual(self.accounts[0].balance, 100)

    def test_withdraw_raise(self):
        with self.assertRaises(ValueError):
            self.accounts[0].withdraw(600)

    def test_transfer(self):
        self.accounts[0].transfer(self.accounts[1], 200)  # С учетом комиссии в 2%
        self.assertEqual(self.accounts[0].balance, 96)
        self.assertEqual(self.accounts[1].balance, 300)

    def test_transfer_raise(self):
        with self.assertRaises(ValueError):
            self.accounts[0].transfer(self.accounts[1], 500)

    def test_full_info(self):
        # Проверяем наличие информации в строке, а не строгий формат
        self.assertIn("300", self.accounts[0].full_info())
        self.assertIn("+79006001020", self.accounts[0].full_info())
        self.assertIn("Петр", self.accounts[0].full_info())

    def test_unique_passport(self):
        with self.assertRaises(ValueError):
            self.accounts.append(Account("Алексей", 12345676, "+79006001020", start_balance=100))


class TestCreditAccount(unittest.TestCase):
    def setUp(self):
        self.accounts = [CreditAccount(name="Петр", passport8=12345678, phone_number="+79006001020", limit=1000,
                                       start_balance=300),
                         CreditAccount(name="Иван", passport8=12345676, phone_number="+79006001020", limit=1000,
                                       start_balance=100)]

    def test_deposit(self):
        self.accounts[0].deposit(500)
        self.assertEqual(self.accounts[0].balance, 800)

    def test_withdraw(self):
        self.accounts[0].withdraw(200)
        self.assertEqual(self.accounts[0].balance, 100)

    def test_withdraw_raise(self):
        with self.assertRaises(ValueError):
            self.accounts[0].withdraw(1600)

    def test_transfer(self):
        self.accounts[0].transfer(self.accounts[1], 200)  # С учетом комиссии в 2%
        self.assertEqual(self.accounts[0].balance, 96)
        self.assertEqual(self.accounts[1].balance, 300)

    def test_transfer_raise(self):
        with self.assertRaises(ValueError):
            self.accounts[0].transfer(self.accounts[1], 1500)

    def test_full_info(self):
        # Проверяем наличие информации в строке, а не строгий формат
        self.assertIn("300", self.accounts[0].full_info())
        self.assertIn("+79006001020", self.accounts[0].full_info())
        self.assertIn("Петр", self.accounts[0].full_info())

    def test_unique_passport(self):
        with self.assertRaises(ValueError):
            self.accounts.append(CreditAccount(name="Алексей", passport8=12345676, phone_number="+79006001020",
                                               limit=100, start_balance=100))
