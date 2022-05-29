# задание 5
# Буфер с сохраненным именем пользователя
user_name = ''


def polite_input(question):
    global user_name
    if (user_name == ''):
        user_name = input('Как Вас зовут?')
    return input(f'{user_name}, {question}')


# age=polite_input('укажите возраст')
# Как Вас зовут?Павел
# Павел, укажите возраст10
# school_number = polite_input('укажите номер школы')
# Павел, укажите номер школы129
# class_num = polite_input('укажите полный номер класса')
# Павел, укажите полный номер класса8Ж