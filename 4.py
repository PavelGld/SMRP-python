# задание 4
# буферы сохраняющие списки взятых предметов и их цен
list_name = []
list_count = []
check_count = 1


def add_item(str, count):
    list_name.append(str)
    list_count.append(count)


def print_receipt():
    global list_name, check_count, list_count
    if (len(list_name) == 0):
        return None
    print("Чек", check_count, ". Всего предметов", len(list_count))
    sum = 0
    for i in range(len(list_count)):
        print(list_name[i], " - ", list_count[i])
        sum += list_count[i]
    print("Итого: ", sum)
    print("-----")
    list_name = []
    list_count = []
    check_count += 1


# add_item('Блокнот', 100)
# print_receipt()

# add_item('Ручка', 70)
# print_receipt()
# print_receipt()

# add_item('Булочка', 15)
# add_item('Булочка', 15)
# add_item('Чай', 5)
# print_receipt()

# add_item('Булочка', 15)
# add_item('Булочка', 15)

# Вывод:
# Чек 1 . Всего предметов 1
# Блокнот  -  100
# Итого:  100
# -----
# Чек 2 . Всего предметов 1
# Ручка  -  70
# Итого:  70
# -----
# Чек 3 . Всего предметов 3
# Булочка  -  15
# Булочка  -  15
# Чай  -  5
# Итого:  35
# -----