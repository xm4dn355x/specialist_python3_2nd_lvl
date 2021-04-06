# Задание: Найдите длину ломаной линии


from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]


def distance(p1: Point, p2: Point) -> float:
    """Расстояние между двумя точками"""
    return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def line_length(points_list: list) -> float:
    """Получает список точек и возвращает длину линии"""
    prev = points_list[0]
    res = 0
    for point in points_list:
        res = res + distance(prev, point)
        prev = point
    return res


if __name__ == '__main__':
    print(f"Длина ломаной линии = {round(line_length(points_list=points), 2)}")
