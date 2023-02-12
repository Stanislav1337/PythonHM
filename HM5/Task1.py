def math(x, y):
    if y == 0:
        return 1
    return math(x, y - 1) * x


A = int(input("Введи число: "))
B = int(input("Введи число для возведения в степень: "))
print(math(A, B))
