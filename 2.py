# задание 2.


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def larger_root(p, q):
    d = discriminant(1, p, q)
    return 0.5 * (-p + (d ** 0.5))


def smaller_root(p, q):
    d = discriminant(1, p, q)
    return 0.5 * (-p - (d ** 0.5))


def main(p, q):
    print(discriminant(1, p, q))
    print(smaller_root(p, q), ' ', larger_root(p, q))


# main(-2.5, 1)
# 2.25
# 0.5   2.0

# print(smaller_root(2, 1))
# -1

# print(larger_root(2, 1))
# -1.0

# print(discriminant(1, 2, 1))
# 0