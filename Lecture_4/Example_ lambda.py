# Анонимные, lambda-функции

# На предыдущей лекции мы с Вами обговорили создание и
# использование функций в Python, но некоторые функции могут
# понадобиться всего раз за всю работу приложения. Как можно
# обойтись без их явного описания? Как сократить подобный код?

def f(x):
    return x ** 2
print(f(5))
a = f
""" Теперь в контексте этого приложения a может использоваться точно так же, как и f.
a — это переменная, которая хранит в себе ссылку на функцию."""

print(a(5))

# Функция в примере занимает всего две строчки кода, но в
# дальнейшем размеры описания функций будут увеличиваться. И
# тогда сокращение кода будет актуальным.

# Пример простой функции, которую будем вызывать(передавать) в другую фунцию 
def calk1(a):
    return a + a

def calk2(a):
    return a * a

def math1(func, val):
    print(func(val))

math1(calk1, 5)

def math2(func, val):
    print(func(val))

math2(calk2, 5)

# Можно передавать несколько аргументов(параметров)
def calk3(a, b):
    return a * b

def math3(func, val_a, val_b):
    print(func(val_a, val_b))

math3(calk3, 5, 12)

# Теперь запишем аналогичный пример через lamda функцию
# def calk4(a):
    # return a * a 
# записали как:
calk4 = lambda a, b : a * b # передаём a, b и : (делаем) a * b
def math4(func, a, b):
    print(func(a, b))
math4(calk4, 5, 14)

# Ещё более короткая запись
math4(lambda a, b : a * b, 5, 14)

# Итак:
# 1. Сначала мы избавились от классического описания функций.
# 2. Затем научились описывать лямбды, присваивая результат какой-то переменной.
# 3. После избавились от этой переменной, пробрасывая всю лямбду в качестве функции.


# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# Через индекс
lst = [1, 2, 3, 5,8, 15, 23, 38]
res_lst = []
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        res_lst.append((lst[i], lst[i]**2))

print(res_lst)

# Через элемент
res_lst2 = []
for i in lst:
    if i % 2 == 0:
        res_lst2.append((i, i**2))

print(res_lst2)

# Более кратко можно записать так
res_lst3 = [(i, i**2) for i in lst if i % 2 == 0]
print(res_lst3)

# Решение через lamda функцию (для общего понимания)
def select(func, val): # Расписаная функция map()  select можно заменить на map()
    return [func(x) for x in val] # Расписаная функция map()

def where(func, val): # Расписаная функция filter()  where можно заменить на filter()
    return [x for x in val if func(x)]

res_lst4 = select(int, lst) # Взяли наш список lst
print(res_lst4)
res_lst4 = where(lambda i: i % 2 == 0, res_lst4) # Нашли только четные элементы
print(res_lst4)
res_lst4 = list(map(lambda i: (i, i**2), res_lst4)) # Возвели их в степень и вывели картежем
print(res_lst4)

