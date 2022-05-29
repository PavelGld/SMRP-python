# задание 14


def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[matrix[i][j] for i in range(n)] for j in range(m)]
    matrix = new_matrix
    return new_matrix

# matrix = [[1, 2, 5], [3, 4, 18]]
# for line in transpose(matrix):
#     print(*line)

# Вывод:
# 1 3
# 2 4
# 5 18
