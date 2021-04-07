import random


class Card:
    """Игральная карта"""
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'
    SUITS = [CLUBS, SPADES, DIAMONDS, HEARTS]
    ICONS = ['♠', '♣', '♦', '♥']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.to_str()

    def __str__(self):
        return self.to_str()

    def __gt__(self, other):    # >
        return self.more(other)

    def __ge__(self, other):    # >=
        return self.more(other) or self.equal(other)

    def __lt__(self, other):    # <
        return self.less(other)

    def __le__(self, other):    # <=
        return self.less(other) or self.equal(other)

    def __eq__(self, other):    # ==
        return self.equal(other)

    def __ne__(self, other):    # !=
        return not self.equal(other)

    def to_str(self):
        """Строковое представление объекта класса карты"""
        return f'{self.ICONS[self.SUITS.index(self.suit)]}{self.value}'

    def equal(self, other_card) -> bool:
        """Проверяет не одинаковые-ли карты"""
        return self.equal_suit(other_card) and self.equal_value(other_card)

    def equal_suit(self, other_card) -> bool:
        """Проверяет одинаковая-ли масть у двух карт"""
        return self.suit == other_card.suit

    def equal_value(self, other_card) -> bool:
        """Проверяет одинаковые-ли значения у карт"""
        return self.value == other_card.value

    def more(self, other_card) -> bool:
        """Сравнивает старше-ли одна карта другой"""
        if self.VALUES.index(self.value) == other_card.VALUES.index(other_card.value):
            return self.SUITS.index(self.suit) > other_card.SUITS.index(other_card.suit)
        else:
            return self.VALUES.index(self.value) > other_card.VALUES.index(other_card.value)

    def less(self, other_card) -> bool:
        """Сравнивает младще-ли одна карта другой"""
        return not self.more(other_card)


class Deck:
    """Карточная колода"""
    def __init__(self):
        self.card_index = 0
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        """Генерирует упорядоченную колоду"""
        self.cards = [Card(value=value, suit=suit) for suit in Card.SUITS for value in Card.VALUES]

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def __getitem__(self, item):
        return self.cards[item]

    def __iter__(self):
        self.card_index = 0
        return self

    def __next__(self):
        card = self.cards[self.card_index]
        self.card_index += 1
        if self.card_index >= len(self.cards):
            raise StopIteration
        return card

    def show(self):
        """Строковое представление колоды"""
        return f'deck[{len(self.cards)}]:{self.cards}'

    def draw(self, count) -> list:
        """Достаёт указанное количество карт из колоды и возвращает список этих карт"""
        cards_in_hand = self.cards[:count]
        self.cards = self.cards[count:]
        return cards_in_hand

    def shuffle(self):
        """Тасует колоду"""
        self.cards = random.sample(self.cards, len(self.cards))


if __name__ == '__main__':
    deck = Deck()
    # Задачи - реализовать нативную работу с объектами:
    # 1. Вывод колоды в терминал:
    print(deck)  # вместо print(deck.show())

    deck.shuffle()
    print(deck)
    card1, card2 = deck.draw(2)
    # 2. Вывод карты в терминал:
    print(card1)  # вместо print(card1.to_str())

    # 3. Сравнение карт:
    if card1 > card2:
        print(f"{card1} больше {card2}")
    else:
        print(f"{card1} меньше {card2}")

    test = card1 >= card2
    print(f'>= {test}')
    test = card1 < card2
    print(f'< {test}')
    test = card1 <= card2
    print(f'<= {test}')
    test = card1 == card2
    print(f'== {test}')
    test = card1 != card2
    print(f'!= {test}')

    # 4. Итерация по колоде:
    for card in deck:
        print(card)

    # Просмотр карты в колоде по ее индексу:
    print(deck[6])

"""
Задания: с колодой карт

Вступление

Вы создали свой класс колоды карт. Пришло время проверить его работу.

Примечание: если какие-то задания не получается выполнить, используя имеющийся функционал, то расширьте его, доработав/изменив/добавив необходимые методы.

Задания

Задание-1

Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху. Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”

Задание-2

Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

Задание-3

Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху. Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой, повторите “перемешать + вытянуть”, до тех пор, пока не вытяните карту больше предыдущей карты. В качестве результата выведи все вытягиваемые карты в консоль.

Задание-4

Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.

Вытягивайте карты парами - одну из первой колоды, вторую из второй.

Если карта из первой колоды окажется больше(старше), то записываем 1:0 (условно начисляем победное очко первой колоде), если карты одинаковые, то не учитываем очко никуда.

Выведите итоговый счет, сравнив попарно все карты в колодах.

Задание-5 “Дурак без козырей”

Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.

Создайте колоду из 52 карт. Перемешайте ее.
Первый игрок берет сверху 6 карт
Второй игрок берет сверху 6 карт.
Игрок-1 ходит:
игрок-1 выкладывает самую маленькую карту по значению
игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
Если игрок-2 не может побить карту, то он проигрывает.
Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
Выведите в консоль максимально наглядную визуализацию данного игрового хода.
Задание-6 “Игра в две колоды”

Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт. Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?
"""