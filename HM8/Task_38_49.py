#  Задача No49. Решение в группах
#  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
#  Фамилия, имя, отчество,
#    номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также
# может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

def input():
    with open("data.txt", "a") as f:
        for i in range(int(input("введите кол-во новых записей в справочник - "))):
            f.write(input("введите ФИО и номер телефона: ") + "\n".upper())


def read():
    with open("data.txt") as f:
        print(f.read())


def find():
    with open("data.txt") as f:
        find_feature = input("введите одну из характеристик для поиска(фио или телефон - ").upper()
        flag = False
        for i in f:
            list_feature = i.split()
            if find_feature in list_feature:
                print(i, end="")
                flag = True
        if not flag:
            print("такой записи не найдено")


def edit():
    edit_data = input("Введите Имя или Фамилию для редактирования записи из справочника : ").upper()
    list1 = []
    with open("data.txt") as f:
        for line in f:
            if edit_data not in line.split():
                list1.append(line)
            else:
                list1.append(input('Введите новые данные: ').upper())
    with open("data.txt", "w") as f:
        f.writelines(list1)


def remove():
    edit_data = input("введите Имя или Фамилию для удаления записи из справочника : ").upper()
    with open("data.txt") as f:
        list_temp = []
        for line in f:
            if edit_data in line.split():
                print(f'{line} удалена ')
                continue
            else:
                list_temp.append(line)
    with open("data.txt", "w") as f:
        f.writelines(list_temp)


while True:
    choice = (int(input(
        """\n введите 1 - для добавления записи,
         2 - для вывода всего справочника, 
         3 - для поиска, 
         4 - для изменения данных
         5 - для удаления данных         
         6 - для завершения работы : """)))
    match choice:
        case 1:
            input()
        case 2:
            read()
        case 3:
            find()
        case 4:
            edit()
        case 5:
            remove()
        case _:
            break