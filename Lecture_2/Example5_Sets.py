# Множества
# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение, пересечение и разность.
# Давайте разберем их.

colors = {'red', 'green', 'blue'}
print(type(colors))
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
colors.clear()
print(colors)
print(type(colors))


# Операции со МНОЖЕСТВОМИ в Python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} - копирует множество
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} - объединяет множество (только уникальные элементы)
i = a.intersection(b) # i = {8, 2, 5} - объединяет пересекающиеся элементы (которые присутствуют в нескольких множествах)
dl = a.difference(b) # dl = {1, 3} - разница между a - b
dr = b.difference(a) # dr = {13, 21} - разница между b - a
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}
#  Пояснение:
"""
1. Объединяем уникальные элементы множества а и b - union()
2. Объединяем пересекающиеся элементы а и b - intersection()
Находим разницу между 1. и 2. - difference()
"""

#  Замороженое множество
set1 = {1, 2, 5}
set_f = frozenset(set1)
print(set_f)
