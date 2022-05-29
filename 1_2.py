# задание 15


def simple_map(transformation, values):
    l = [transformation(i) for i in values]
    return l


# values = [1, 3, 1, 5, 7]
# print(*simple_map(lambda x: x + 5, values))
# Вывод: 6 8 6 10 12