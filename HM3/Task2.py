# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import os
import random
os.system('CLS')

list = []
num = int(input("Введите число элементов в массиве (1-60): "))
a = int(input("Введите натуральное число (0-50): "))

list.append(random.randint(0,20))
difference = abs(a-list[0])
b = 0

for i in range (1,a):
    list.append(random.randint(0,20))
    if (abs(a-list[i]) < difference):
        difference = abs(a-list[i])
        b = i

print("Cлучайно заданный масиив:")
print(list)
print(f"Является самым ближайшим : {list[b]}")