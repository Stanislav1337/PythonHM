# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input('Введите число: ')

a=int(number[-3])
b=int(number[-2])
c=int(number[-1])


print(a + b + c)
