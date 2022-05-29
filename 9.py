# задание 9
# Ошибка в "sequence = sequence + [next_element] " Оно пересоздает новый массив и записывает его. В остальном все верно
# Вариант исправления:


def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)  # append добавляет элемент в конец


# sequence = [1, 1]
# continue_fibonacci_sequence(sequence, 1)
# print(*sequence)
# Вывод:1 1 2

# sequence = [1, 1, 2, 3, 5]
# continue_fibonacci_sequence(sequence, 0)
# print(*sequence)
# Вывод:1 1 2 3 5