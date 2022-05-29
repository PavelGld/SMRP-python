# Задание 11_1
def equation_plus(val):
    val += added_part
    return val


def value_plus(val):
    val = val + added_part
    return val

# Приведем пример в виде суммы 2 списков. переменные попарно ссылаются на 1 адрес
# как видно в случае += выводится объединение списков ( добавился элемент )
# в случае + пересоздается переменная и в неё вписывается новое значение
n1 = n2 = [1]
m1 = m2 = [1]
added_part = [4]
equation_plus(n1)
value_plus(m1)
print(n2)
print(m2)

# Вывод:
# [1, 4]
# [1]