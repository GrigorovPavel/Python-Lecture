# Функция zip

# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
# из элементов входных данных

# Пример:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Функция zip () пробегает по минимальному входящему набору:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

# Пример
students = ['Вася', 'Петя', 'Коля', 'Дима']
estim = [3, 5, 4, 5]
stependia = [0, 200, 100, 200]
res_lst = list(zip(students, estim, stependia))
print(res_lst)
