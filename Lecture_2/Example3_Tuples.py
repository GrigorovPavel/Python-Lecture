# Кортежи

# Кортеж — это неизменяемый список.
# Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты каких-либо
# данных от изменений (намеренных или случайных). Кортеж занимает меньше места в
# памяти и работают быстрее, по сравнению со списками
"""
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
"""

t = ()
print(type(t)) # <class 'tuple'>
t = (7789)
print(type(t)) # <class 'int'>

t = (7789,) # после значения, необзодимо ставить запятую
print(type(t)) # <class 'tuple'>
t = (1, 2, 3, 8, 7,)
print(type(t)) # <class 'tuple'>

# Сделать из Списка Кортеж
v = [1, 6, 9] # список
print(v)
print(type(v)) # <class 'list'>

v = tuple(v) # список конвертируем в кортеж
print(v)
print(type(v)) # < class 'tuple'>

#  Ещё пример:
a_list = [1, 2, 3, 4, 5] 
b_tuple = tuple (a_list) 
print (type (b_tuple)) # < class 'tuple'>

#  Кортеж можно разделить на переменные:
"""
a, b, c = 1, 6, 9 - Множественное присваивание
"""
a, b, с = v # присваиваем переменным значения из кортежа
print(a, b, с) # отдельные переменные
print(v) # < class 'tuple'>

# Обращение к элементам по индексу
print(v[2]) # выведется 3й элемент (с индексом 2)

# Можно пройти циклом for по элементам кортежа
for i in v:
    print(i) # Выводим элементы по очередно
#  или
for i in range(len(v)):
    print(v[i])

# Ещё пример:
# Можно распаковать кортеж в независимые переменные:
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue