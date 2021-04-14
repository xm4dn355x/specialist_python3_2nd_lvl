# from generators import get_user_data
from abc import ABC, abstractmethod
from datetime import datetime

EMPLOYEE_PASSWORD = "123"


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        pass

    @abstractmethod
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"..."

    @abstractmethod
    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"..."


class Account(AccountBase):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        super().__init__(name, passport8, phone_number, start_balance)
        self.history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if self.balance + amount < 0:
            raise ValueError('введено отрицательное число')
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        return amount

    def add_to_history(self, timestamp: datetime, operation: str, amount: int):
        self.history.append({'timestamp': timestamp, 'operation': operation, 'amount': amount})

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."


if __name__ == '__main__':
    ivan = Account('Иван', '12345678', 90000000000, start_balance=1000)
    oleg = Account('Иван', '23456789', 90000000001, start_balance=10000)
    print(ivan)
    print(oleg)
    ivan.deposit(100)
    print(ivan)
    try:
        ivan.withdraw(1000000)
    except ValueError as e:
        print(e)
    print(ivan)
    try:
        ivan.transfer(oleg, 1000000)
    except ValueError as e:
        print(e)
    print(ivan)
    print(oleg)
    ivan.transfer(oleg, 500)
    print(ivan)
    print(oleg)