# Функция enumerate

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.
# Функция enumerate() позволяет пронумеровать набор данных.

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# Можно указать стартовый индекс
users = ['user1', 'user2', 'user3']
data = list(enumerate(users, 1)) #  1 - startIndex -> [(1, 'user1'), (2, 'user2'), (3, 'user3')]
print(data)