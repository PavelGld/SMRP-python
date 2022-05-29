# задание 27
from math import ceil

list_line = []

population = {}
# составление списка строк
for line in sys.stdin:
    if line.strip() == "exit":
        break
    list_line.append(line.split())

for i in list_line:
    # выделение названия столицы из строки, а затем диапазона популяции(по верхней границе через ceil)
    name = i[0]
    pop = int(ceil(int(i[2])/100000)) * 100
    # Если уже были города  с такой популяцией, то город добавляется в список, иначе такой список создается
    if pop not in population:
        population[pop] = [name]
    else:
        population[pop].append(name)

# Сортировка по числу жителей
population_list = sorted(population)
for i in population_list:
    print(i-100, ' - ', i, ':', ", ".join(population[i]))

# Ввод:
# Братислава Словакия 625167
# Брюссель Бельгия 1154635
# Будапешт Венгрия 1757618
# Белград Сербия 1233796
# Прага Чехия 1267449
# София Болгария 1286383
# Тбилиси Грузия 1118035

# Вывод:
# 600  -  700 : Братислава
# 1100  -  1200 : Брюссель, Тбилиси
# 1200  -  1300 : Белград, Прага, София
# 1700  -  1800 : Будапешт