# задание 26

from functools import reduce
from math import gcd
import sys
list_line = []

# составление списка строк
for line in sys.stdin:
    if line.strip() == "exit":
        break
    list_line.append(line)
# перевод строк в числа для определения НОД
num_list = list(map(int, list_line))
# через reduce производится вычисление НОД'ов в результате получается общих НОД
print(reduce(lambda x, y: gcd(x, y), num_list))

# Ввод:
# 36
# 12
# 144
# 18
# Вывод:
# 6