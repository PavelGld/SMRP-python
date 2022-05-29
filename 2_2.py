# задание 16


def find_num():
    # Внешняя сумма производит сумму квадратов, фильтр отбирает числа не делящиеся на 9, двузначность указана в range()
    return sum(map(lambda x: x ** 2, filter(lambda x: not x % 9, range(10, 100))))

# print(find_num())
# Вывод: 40905