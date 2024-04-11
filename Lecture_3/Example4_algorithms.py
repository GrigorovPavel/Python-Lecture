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
    


# Пример 

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