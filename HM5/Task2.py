# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
def sum_AB (a, b):
    if a == 0:
        if b == 0:
            return 0
        return sum_AB(a, b - 1) + 1
    return sum_AB(a - 1, b) + 1


n1 = int(input("введи 1-е число: "))
n2 = int(input("введи 2-е число: "))
print(sum_AB(n1, n2))
