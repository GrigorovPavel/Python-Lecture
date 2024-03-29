# Словари
# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).

d =  {} # создали пустой словырь
d = dict() # создали пустой словарь

d['q'] = 'qwerty'
print(d) 
d['1'] = '12345'
print(d) # Выводятся все значения словаря
print(d['q']) # Выводится элемент, которому соответствует ключ

# Ещё пример
dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'  # можно добавить или изменить элемент
print(dictionary['left']) # ⇐ 
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
print(dictionary) # {'up':'↑', 'down':'↓', 'right':'→'}

# Взаимодействие цикла for со словарём

for item in dictionary:
    print(item) # Выводятся значения КЛЮЧЕЙ

for item in dictionary:
    print('{} -> {}'.format(item, dictionary[item])) # Выводим ключ и значение элемента
    # {} - пустые словари в которые поместится результат функции .format() - в которую передано два аргумента
# up -> ↑
# down -> ↓
# right -> →

# Можно сделать таким образом:
print(dictionary.items())   # dict_items([('up', '↑'), ('down', '↓'), ('right', '→')])    
for (k,v) in dictionary.items():
    print(k,v)
# up ↑
# down ↓
# right →


