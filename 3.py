# задание 3.

# буфер в который сохраняются не дублированные сообщения, для последующего вывода

message_list = []


# Функция проверки на повтор и записи
def print_without_duplicates(mess):
    if mess not in message_list:
        message_list.append(mess)


# print_without_duplicates("Привет")
# print_without_duplicates("Не могу до тебя дозвониться")
# print_without_duplicates("Не могу до тебя дозвониться")
# print_without_duplicates("Не могу до тебя дозвониться")
# print_without_duplicates("Когда доедешь до дома")
# print_without_duplicates("Ага, жду")
# print_without_duplicates("Ага, жду")

# Вывод итогового сообщения. join переделывает буфер в строку.
# Если по хорошему надо бы сделать класс для этой функции чтобы буфер не валялся в общем пространстве,
# но это противоречит заданию
# print("\n".join(message_list))
# Вывод:
# Привет
# Не могу до тебя дозвониться
# Когда доедешь до дома
# Ага, жду