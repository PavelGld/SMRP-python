# Задание 10_2

from itertools import permutations


def decrypting(listing, text):
    listing = listing.lower().split()
    text = text.lower().split()
    list_permute = []
    for i in listing:
        str_permute = ""
        permute = permutations(i)
        for j, v in enumerate(permute):
            if j != 0:
                word = ""
                for k in v:
                    word += k
                str_permute += word + " "
        str_permute = str_permute.split()
        list_permute += str_permute

    new_text = text.copy()
    for i in text:
        if i in list_permute:
            put = ""
            while len(put) < len(i):
                put += "#"
            num = new_text.index(i)
            new_text.remove(i)
            new_text.insert(num, put)

    print(*new_text)


diction = "привет ток кот моток места ночь ночи есть тесть геолокация Надя" # str(input())
letter = "Привет Доехали до места к ночи Здесь есть кот гладим его Даня"  # str(input())

decrypting(diction, letter)
# Ввод:
# привет ток кот моток места ночь ночи есть тесть геолокация Надя
# Привет Доехали до места к ночи Здесь есть кот гладим его Даня

# Вывод:
# привет доехали до места к ночи здесь есть ### гладим его ####