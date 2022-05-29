# Задание 7_2

# функция удаления лишних символов


def sorting(text):
    for i in text:
        if i in ".,;:!&?*'\"":
            text = text.replace(i, " ")
    return text
# подсчет и сортировка


def counting(text):

    text = list(sorting(text).split())
    new_words = []

    for i, v in enumerate(text):
        for j in v:
            if j.isupper():
                if v not in str(new_words):
                    new_words += [[v,  i]]
    new_words = sorted(new_words)

    for i, v in enumerate(new_words):
        print(new_words[i][1], "-", new_words[i][0])


text = "\n".join(iter(input, ""))

counting(text)
# Ввод:
# Ехал Грека через реку.
# Видит Грека в реке рак.
# Сунул в реку руку Грека.
# Рак за руку Греку цап.

# Вывод:
# 4 - Видит
# 1 - Грека
# 17 - Греку
# 0 - Ехал
# 14 - Рак
# 9 - Сунул