# задание 7
# Буфер с записями оплаты
daily_food = [0, 150, 150]


# функция суммы оплаты. i-1 сдвиг т.к. отсчет python идет с 0
def count_food(days):
    return sum([daily_food[i - 1] for i in days])


# print(count_food([1]))
# print(count_food([2, 3]))
# Вывод
# 0
# 300
