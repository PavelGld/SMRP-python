# задание 13

a = [77, 33]


def from_string_to_list(string, container):
    for i in string.split():  # разделение строки на список чисел
        if i.isdigit():  # проверка является ли набор символов целым числом
            a.append(int(i))

# from_string_to_list("33 34 45 abc", a)
# print(a)
# Вывод: [77, 33, 33, 34, 45]
