# "Друзья друзей"
# У всех людей, по крайне мере я надеюсь, есть друзья. У ваших друзей тоже есть друзья и так далее.
# Вы решили запустить свой бизнес и пригласить максимальное количество людей на его открытие.
# Вам в руки попала, как нельзя кстати, база людей со списком их друзей.
# Считаем, что комбинация Имя+Фамилия нам позволяет однозначно идентифицировать человека.

# Задача
# По предоставленным данным(файл peoples.json) определите:
# 1. Сколько людей придет на открытие, если вы отправляете приглашение конкретному человеку
# (любому, на ваш выбор, из базы), а тот всем друзьям, друзья друзьям и т.д.

# 2. Какому минимальному числу людей, нужно отправить приглашение,
# чтобы пришли ВСЕ люди, присутствующие в базе?


import json


def find_a_way(start=0, finish=0, graph=None, check_all=False):
    visited = [False] * (len(graph))
    def dfs(v):
        visited[v] = True
        for w in graph[v]['friends']:
            if not visited[w]:  # посещён ли текущий сосед?
                dfs(w)
    dfs(start)
    if check_all:
        return visited
    return visited[finish]

def bfs_friends(graph, start):
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]['friends']:
            for human in graph:
                if vertex['name'] == human['name'] and vertex['surname'] == human['surname']:
                    vertex = graph.index(human)
                    break
            try:
                if lengths[vertex] is None:
                    lengths[vertex] = lengths[cur_vertex] + 1
                    queue.append(vertex)
            except TypeError:
                pass
    return lengths


def find_coverage(graph: list, name, surname):
    pass


with open('people.json', 'r') as f:
    data = json.load(f)
    print(data[0]['friends'])
    for i in range(len(data)):
        print(i)
        all = bfs_friends(data, i)
        print(all)