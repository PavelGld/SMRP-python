# Задание 14_2

def Hemateria(list_of_words):
    ords = []
    for i in list_of_words:
        summ = 0
        for j in i:
            summ += ord(j.upper()) - ord('A') + 1
        ords += [[summ]]
    for j, v in enumerate(ords):
        v.insert(1, list_of_words[j])
    ords = sorted(ords)

    for j, v in enumerate(ords):
        print(v[1])


list_of_words = "\n".join(iter(input, "")).split()

Hemateria(list_of_words)


# Ввод:
# mother
# Daddy
# sIster

# Вывод:
# Daddy
# mother
# sIster

# Ввод:
# bBb
# aaaaaa
# word

# Вывод:
# aaaaaa
# bBb
# word

