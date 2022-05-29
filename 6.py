# задание 6
# словарик с сетами друзей. Сеты позволяют задать множество друзей без повторений
# , а словарь позволяет быстро делать одностороннюю проверку
name_dict = {}


def add_friends(name, friend_name):
    global name_dict
    if name in name_dict:
        name_dict[name] = name_dict[name].union(set(friend_name))
    else:
        name_dict[name] = set(friend_name)


def are_friends(name1, name2):
    return name2 in name_dict[name1]


def print_friends(name_of_person):
    return name_dict[name_of_person]


# add_friends("Алла", ["Марина", "Иван"])
# print(are_friends("Алла", "Мария"))
# add_friends("Алла", ["Мария"])
# print(are_friends("Алла", "Мария"))
# Выход:
# False
# True