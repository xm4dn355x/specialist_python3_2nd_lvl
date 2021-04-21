# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from deck import Deck, Card

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()


def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    for card in cards:
        print(card)
        if card.value == 'J' or card.value == 'Q' or card.value == 'K':
            weight = 10
        elif card.value == 'A':
            weight = 11
        else:
            weight = int(card.value)
        sum_points += weight
    print(f'{sum_points=}')
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points = 0
        for card in cards:
            if card.value == 'J' or card.value == 'Q' or card.value == 'K':
                weight = 10
            elif card.value == 'A':
                weight = 1
            else:
                weight = int(card.value)
            sum_points += weight
        return sum_points
    return sum_points


while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f'player cards {player_cards}')
    print(f'dealer cards {dealer_cards}')
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards.append(deck.draw(1)[0])
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                # TODO: здесь дилер берёт карты
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) < 21:
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            if sum_points(dealer_cards) == 21:
                print('У дилера 21!')
                break
            elif sum_points(dealer_cards) < 17:
                dealer_cards.append(deck.draw(1)[0])
                print(f'Дилер взял ещё карту: {dealer_cards}')
            else:
                print(f'Дилер закончил добирать карты. его рука: {dealer_cards}')
                break
    print(f'{player_cards=} {dealer_cards=}')
    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) > 21:
        print(f'Игрок проиграл набрав {sum_points(player_cards)} очков')
    elif sum_points(dealer_cards) > 21:
        print(f'Игрок победил, так как у дилера перебор {sum_points(dealer_cards)} очков')
    if sum_points(player_cards) > sum_points(dealer_cards):
        print(f'Игрок победил! игрок набрал {sum_points(player_cards)}, а дилер {sum_points(dealer_cards)}')
    else:
        print(f'Дилер победил! игрок набрал {sum_points(player_cards)}, а дилер {sum_points(dealer_cards)}')