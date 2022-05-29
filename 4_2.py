# задание 18

def is_rifm(str):
    # Разделение на строки с рифмой и приведение строк к нижнему регистру
    list_string = str.lower().split()
    # словарь гласных
    s = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    # суммирование гласных для оценки рифмы посредством лямбда функции
    rifm_list = [(lambda x: sum(1 for i in x if i in s))(i) for i in list_string]
    # Проверка одинаковы ли они
    for i in range(1, len(rifm_list)):
        if rifm_list[i] != rifm_list[i-1]:
            print("Пам парам")
            return 0
    print("Парам пам-пам")
    return 1

# is_rifm("пара-ра-рам рам-пам-папам па-ра-па-дам")
# Вывод : Парам пам-пам