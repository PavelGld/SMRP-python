# задание 17

values = [1, 23, 42, "asdfg"]
transformation = lambda x: x
# Лямбда выражение которое меняет элемент x на x.
# по сути мы не изменяем элемент поданный на трансформацию
transformed_values = list(map(transformation, values))

# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')
# Вывод: ok