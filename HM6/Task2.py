# # Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:
# [-5,9,0,3,-1,-2,1,4,-2,1-,2,0,-9,8,10,-9,0,-5,-5,7]
# 5
# 15
# Вывод: [1,9,13,14,19]

list = [-5, 9, 0, 3, -1, -2, 1, 4,-2, 1, -2, 0,- 9, 8, 10, -9, 0, -5, -5, 7]
min = int(input("введите максимальное число: "))
max = int(input("введите минимальное число: "))

print(*[i for i in range(len(list)) if min <= list[i] <= max])