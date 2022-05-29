# задание 19


def same_by(function, value):
    return len(set(map(function, value))) == 1 if value else True

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# Вывод same

# values = [1, 2, 3, 4]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# Вывод different