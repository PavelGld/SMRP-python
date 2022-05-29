# задание 10
# reverse изменяет сам массив!!!!

# Вариант исправления:

def mirror(arr):
    mirror_arr = arr[::-1]  # Через срез берутся все элементы но с конца с шагом 1
    arr += mirror_arr


# arr = [1, 2]
# mirror(arr)
# print(*arr)
# Вывод:1 2 2 1

# arr = [1]
# mirror(arr)
# print(*arr)
# Вывод:1 1
