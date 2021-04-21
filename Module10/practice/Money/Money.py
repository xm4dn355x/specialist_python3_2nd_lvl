class Money:
    def __init__(self, whole=0, fractional=0):
        self.value = (whole * 100) + fractional
        self.name = 'Рубль'
        self.name_plural = 'Рубли'

    def __str__(self):
        return f'{self.name_plural} {self.value // 100}.{self.value % 100}'

    def __add__(self, other):
        return Money(((self.value + other.value) // 100), ((self.value + other.value) % 100))

    def __sub__(self, other):
        return Money(((self.value - other.value) // 100), ((self.value - other.value) % 100))


if __name__ == '__main__':
    money1 = Money(1, 30)
    money2 = Money(1, 70)
    money3 = money1 + money2
    print(money1)
    print(money1.value)
    print(money2)
    print(money2.value)
    print(money3)
    print(money3.value)
    money4 = money3 - Money(1, 1)
    print(money4)