# задание 25
from functools import reduce
import sys

list_line = []

# составление списка строк
for line in sys.stdin:
    if line.strip() == "exit":
        break
    list_line.append(line)


# Считывание данных с консоли, после удаления пробелов в начале и конце через strip.
# Через replace удаляется переход на новую строку
result_text = [i.replace("/n", "") for i in map(str.strip, list_line)]
# через reduce сортируется по возрастанию и выводится максимальное значение
print(reduce(lambda x, y: sorted([x, y])[0], result_text))

# Ввод:
# котик
# тюлень
# кашалот
# нарвал
# exit
# Вывод:
# кашалот
