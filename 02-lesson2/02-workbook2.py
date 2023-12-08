print("Калькулятор")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("1. Сложить\n2. Вычесть\n3. Умножить\n4. Поделить")
operand = int(input("Выберите действие: "))
if operand == 1:
    print("Ответ: " + str(num1+num2))
elif operand == 2:
    print("Ответ: " + str(num1-num2))
elif operand == 3:
    print("Ответ: " + str(num1*num2))
elif operand == 4:
    print("Ответ: " + str(num1/num2))
else:
    print("Такого действия нет")
# ДЗ:
# Доделать поиск остатка от деления и целую часть от деления

