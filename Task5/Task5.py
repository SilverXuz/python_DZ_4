"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
"""

# Это максимальное кривое и костыльное решение, которое я смог из себя выжать.
# Понятия не имею будет ли это работать с другими значениями, и насколько корректно вообще делать сортировку такого рода.
# Логика сортировки состоит в том, что множитель икса всегда первый, а степень всегда вторая в списке.

#  Выгрузка строки из первого файла
path = 'mn1.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

#  Выгрузка строки из второго файла
path1 = 'mn2.txt'
data1 = open(path1, 'r')
for line1 in data1:
    print(line1)
data1.close()

# Разбиение строки по пробелу
test = line.split(' ')
test1 = line1.split(' ')

# Проверка элемента списка на число
proverka = []
s = []
for i in test:
    try:
        num = int(i)
        cf = True
    except:
        cf = False
    if cf == True:
        proverka.append(num)
for i in range(len(proverka)): # Сортировка и перезапись только тех значений, которые стоят на нечетных позициях.
    if not i % 2:
        s.append(proverka[i])
print(s)    

# Собственно такой же цикл проверок для второго списка, как и выше.
proverka1 = []
s1 = []
for i in test1:
    try:
        num = int(i)
        cf = True
    except:
        cf = False
    if cf == True:
        proverka1.append(num)
for i in range(len(proverka1)):
    if not i % 2:
        s1.append(proverka1[i])
print(s1) 

# Суммирование значений элементов двух отсортированных списков
result = list(map(sum, zip(s,s1)))
print(result)

# Запись полученных результатов в новый шаблон многочлена и его запись в новый файл.
l = 3
list_mn = []
j = len(result)
for i in result:
    if j == 1:
        list_mn.append(i)
    else:
        mn = f'{i} * x ^ {j - 1}'
        list_mn.append(mn)
        j -= 1

print(" + ".join(map(str, list_mn)) + " = 0")
with open('mn_new.txt', 'w') as data:
    data.write(" + ".join(map(str, list_mn)) + " = 0")
    print('Третий файл записан!')
