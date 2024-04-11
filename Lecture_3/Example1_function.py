# Функции
# Функция — это фрагмент программы, используемый многократно.
# Мы знакомы уже с функциями с C#, давайте теперь посмотрим, как
# создаются и используются функции внутри Python

# def function_name(x):

# Задача
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.

# Решение:
# 1. Необходимо создать функцию:

def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa) # возвращает print()
num = 5
res = sumNumbers(num)

# функция возвращает значение (результат)
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa # функция возвращает значение (результат)
num = sumNumbers(6)
print(num)


# В функции можно передавать несколько аргументов
def mult(a, b):
    c = a * b
    return c
print(mult(5, 9))

def mult(a, b, c = "$"):
    res = a * b
    print(res, c)
mult(10, 4) # 'c' - не передаем, оно указано по умолчанию

def mult(a, b, c = "$"):
    res = a * b
    print(res, c)
mult(10, 4, "руб.") # 'c' - передаем


# Если мы не знаем сколько аргументов будет передоваться в функцию 
# можно записать так:
def sum_str(*args):
    res = ""
    for i in args:
        res += i
    return res
print(sum_str('1' 'q' '2' 'w'))