# Алгоритмы
# Алгоритмом называется набор инструкций для выполнения
# некоторой задачи. В принципе, любой фрагмент
# программного кода можно назвать алгоритмом, но мы с
# Вами рассмотрим 2 самых интересных алгоритмы
# сортировок:
# ● Быстрая сортировка
# ● Сортировка слиянием

# ● Быстрая сортировка
def quick_sort(arr):
    for i in range(1, 101):
        if len(arr) <=1:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([7, 9, 11, 13, 15, 17, 58, 32, 1, 78, 61, 18]))
    
# Ещё пример 
def quicksort(array):
    print(array)
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))
#  Пояснение
"""
● 1-е повторение рекурсии:
○ array = [10, 5, 2, 3]
○ pivot = 10
○ less = [5, 2, 3]
○ greater = []
○ return quicksort([5, 2, 3]) + [10] + quicksort([])

● 2-е повторение рекурсии:
○ array = [5, 2, 3]
○ pivot = 5
○ less = [2, 3]
○ greater = []
○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что здесь помимо вызова рекурсии
добавляется список [10]
● 3-е повторение рекурсии:

○ array = [2, 3]
○ return [2, 3] # Сработал базовый случай рекурсии
На этом работа рекурсии завершилась и итоговый список будет выглядеть таким образом: [2, 3] + [5] + [10] = [2, 3, 5,10]
"""

# ● Сортировка слиянием

