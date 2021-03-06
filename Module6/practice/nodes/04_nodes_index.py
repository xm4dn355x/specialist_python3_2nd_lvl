class Node:
    """Класс для узла списка. Хранит значение и указатель на следующий узел."""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def len_nodes(start_node):
    """
    Возвращает целое число - кол-во нод у цепочке
    """
    count = 1
    node = start_node
    while node.next:
        count += 1
        node = node.next
    return count


def print_node_by_index(start_node, index):
    """
    Выводит в терминал значение(value) ноды с заданным индексом(index). Индексация начинается с нуля.
    Если index = 0, выводим значение ноды start_node
    Считаем, что index гарантированно > 0
    """
    iter = 0
    while iter != index:
        start_node = start_node.next
        iter += 1
    print(start_node.value)


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


if __name__ == '__main__':
    # Дан список из произвольного количества имен
    names = gen_names_list()
    print(names)

    # TODO: скопируйте цепочку нод из предыдущей задачи
    prev = None
    for name in names:
        node = Node(value=name, next=prev)
        prev = node


    # TODO: Передайте первую ноду и индекс ноды, значение которой нужно вывести, в функцию print_node_by_index()
    #  напишите реализацию функции print_node_by_index()
    first_node = node
    index = 2
    print_node_by_index(first_node, index)