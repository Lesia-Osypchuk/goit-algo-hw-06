def dfs(graph, start, end, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    visited.add(start)
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in visited:
            new_paths = dfs(graph, node, end, path, visited)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def bfs(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph[vertex]:
            if next_node not in visited:
                visited.add(next_node)
                if next_node == end:
                    yield path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))

# Задаємо граф метро міста Києва (той самий граф, який був створений у першому завданні)
metro_graph = {
    "Шулявська": {"Політехнічний інститут"},
    "Політехнічний інститут": {"Шулявська", "Вокзальна"},
    "Вокзальна": {"Політехнічний інститут", "Університет"},
    "Університет": {"Вокзальна", "Театральна / Золоті ворота"},
    "Театральна / Золоті ворота": {"Університет", "Хрещатик / Майдан незалежності", "Лук'янівська", "Палац спорту / Площа українських героїв"},
    "Хрещатик / Майдан незалежності": {"Театральна / Золоті ворота", "Арсенальна", "Поштова Площа",  "Палац спорту / Площа українських героїв"},
    "Арсенальна": {"Хрещатик / Майдан незалежності", "Дніпро"},
    "Дніпро": {"Арсенальна", "Гідропарк"},
    "Гідропарк": {"Дніпро"},
    "Дорогожичі": {"Лук'янівська"},
    "Лук'янівська": {"Театральна / Золоті ворота", "Дорогожичі"},
    "Палац спорту / Площа українських героїв": {"Театральна / Золоті ворота", "Кловська", "Олімпійська"},
    "Кловська": {"Палац спорту / Площа українських героїв", "Печерська"},
    "Печерська": {"Кловська", "Звіринецька"},
    "Звіринецька": {"Печерська", "Видубичі"},
    "Видубичі": {"Звіринецька"},
    "Поштова Площа": {"Хрещатик / Майдан незалежності", "Контрактова Площа"},
    "Контрактова Площа": {"Поштова Площа"},
    "Олімпійська": {"Палац спорту / Площа українських героїв", "Палац Україна"},
    "Палац Україна": {"Олімпійська"}
    }

# Задаємо початкову та кінцеву вершини
start_station = "Політехнічний інститут"
end_station = "Палац Україна"

# Знаходимо шляхи за допомогою DFS та BFS
dfs_paths = dfs(metro_graph, start_station, end_station)
bfs_paths = list(bfs(metro_graph, start_station, end_station))

# Виводимо результати
print("Шляхи знайдені за допомогою DFS:")
for path in dfs_paths:
    print(path)
print("\nШляхи знайдені за допомогою BFS:")
for path in bfs_paths:
    print(path)