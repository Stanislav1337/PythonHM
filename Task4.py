# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите число: '))
m = int(input('Введите число: '))
k = int(input('Введите число: '))



if k < m*n :

    print('YES')

else: print('NO')