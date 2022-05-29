def translate(my_str):
    list_zam = {'а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я', ',', '.', ';', 'А', 'О', 'Э', 'Е', 'И', 'Ы', 'У', 'Ё',
                'Ю', 'Я'}
    my_str = my_str
    new_str = ""
    # удаление гласных и знаков припинания
    for j in range(len(my_str)):
        if my_str[j] not in list_zam:
            new_str += my_str[j]

    # удаление появившихся пробелов
    result_str = ""
    for j in range(len(new_str)):
        if (j + 1 != len(new_str)):
            if (new_str[j] + new_str[j + 1] != "  "):
                result_str += new_str[j]
        else:
            result_str += new_str[j]

    return result_str


# str = "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать."
# print(translate(str))
# "двтльнй фкт н ткст н зк НРЗБРЧВ кзвтс двльн прст чтть Дсттчн нбльшй трнрвк - в смжт т длть"