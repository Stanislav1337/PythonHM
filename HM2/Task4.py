# Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 0, 1, 2, 3

n = int(input("Введите число: "))
k = 0

while (2**k <= n):
    print(k)
    k +=1