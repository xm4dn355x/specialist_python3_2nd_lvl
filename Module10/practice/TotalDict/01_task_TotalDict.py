# Разработать класс TotalDict со следующими возможностями:
class TotalDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'TD:{super().__str__()}'

    def __add__(self, other):
        total = self.copy()
        for key, value in other.items():
            if total.get(key):
                total[key] += value
            else:
                total[key] = value
        return TotalDict(total.items())

    def __sort_by_value(self):
        return sorted(self.items(), key=lambda x: x[1], reverse=True)

    def most_expensive(self, count=0):
        items = self.__sort_by_value()
        if count == 0:
            return items
        elif count < 0 or type(count) != int:
            raise ValueError('Только целое положительное число')
        else:
            return items[:count]


# 1. Объект выводит себя в консоли как обычный словарь, НО с символами TD: в начал
items1 = TotalDict(milk=250, bread=120, meat=450.6)
items2 = TotalDict(juice=99.9, fish=120, milk=50.2)
print(items1)  # TD:{'milk': 250, 'bread': 120, 'meat': 450.6}
print(items2)
# 2. При сложении объектов TotalDict значения элементов с одинаковыми ключами суммируются
all_items = items1 + items2
print(all_items)  # TD:{'milk': 300.2, 'bread': 120, 'meat': 450.6, 'juice': 99.9, 'fish': 120}

# 3. Добавить метод .most_expensive() выводящий все элементы в виде списка кортежей,
# упорядоченного по убыванию по значениям
print(all_items.most_expensive())  # [('meat', 450.6), ('milk', 300.2), ('bread', 120), ('fish', 120), ('juice', 99.9)]

# 4. Метод .most_expensive() можно передать целое число, ограничивающее кол-во возвращаемых значений
print(all_items.most_expensive(3))  # [('meat', 450.6), ('milk', 300.2), ('bread', 120)] <-- только 3 кортежа