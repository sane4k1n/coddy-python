# 11 45 Saturday
# Условный оператор
# if - если
# elif -> else + if -> иначе если, доп. условие
# else - иначе
# condition(условие), action(действие)
# if condition:
#   action1
# elif condition2:
#   action2
# else:
#   action3
# > - больше, >= больше или равно
# (condition) -> True or False
#Нужно ввести 2 слова, вывести большее
#Подумать: как сравниваются слова
# len() - ф-ция нахождения длины
# Задание:
# Ввести 3 фамилии, вывести их в порядке алфавитного списка
# Пример:
# Абрамов
# Гладышев
# Булкин
# Вывод:
# Абрамов Булкин Гладышев
a = input("Введите 3 фамилии:\n")
b = input()
c = input()
if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < c < a:
    print(b, c, a)
elif b < a < c:
    print(b, a, c)
elif c < a < b:
    print(c, a, b)
elif c < b < a:
    print(c, b, a)
# DZ:
# Ввести 3 числа, вывести наибольшее








