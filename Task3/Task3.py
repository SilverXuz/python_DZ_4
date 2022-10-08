"""
Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""

# Не мое решение. Но осознанное) 

lst = [3, 7, 'nine', 3, 5, 'nine', 'four', 7, 2, 1, 4]
print(f'Исходный список: {lst}')
enpty_lst = []

def double_num(lst, value):
    count = 0
    for i in range(len(lst)):
        if lst[i] == value:
            count += 1
    return count

def save_num(lst):
    enpty_lst = []
    for i in range(len(lst)):
        if double_num(lst, lst[i]) == 1:
            enpty_lst.append(lst[i])
    return enpty_lst

print(f'Список уникальных значений: {save_num(lst)}')
