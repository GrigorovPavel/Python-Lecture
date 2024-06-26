# List Comprehension
"""
У каждого языка программирования есть свои особенности и преимущества. 
Одна из культовых фишек Python — list comprehension (редко переводится на русский, но можно использовать определение «генератора списка»).
Comprehension легко читать, и их используют как начинающие, так и опытные разработчики.
List comprehension — это упрощенный подход к созданию списка, который задействует 
цикл for, а также инструкции if-else для определения того, что в итоге окажется в финальном списке.
"""
# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]

# 1. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]


# Task_1
# Создать список, состоящий из чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i) # добавляем к конци списка новое значение(каждую итерацию)
print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]


# Task_2
# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]






