"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

N = int(input('Задайте натуральное число: '))
result = []
p = 2

while p != N:
        if N % p == 0:
            N /= p
            result.append(p)
        else:
            p +=1
else:
    result.append(p)
print(result)


# 2
# n = int(input('Введите натуральное число: '))
# if n > 0:
#     multipliers = []
#     while n > 1:
#         for i in range(2, n + 1):
#             count = True
#             for j in range(2, i):
#                 if i % j == 0:
#                     count = False
#                     break
#             if count:
#                 while n % i == 0:
#                     multipliers.append(i)
#                     n /= i
#     print(multipliers)
# else:
#     print('Введено не натуральное число')



# Виталий 
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число N = '))
# prime_number = 2
# list_factor = []

# while prime_number != n:
#     if n % prime_number == 0:
#         n /= prime_number
#         list_factor.append(prime_number)
#     else:
#         prime_number += 1
# #if n == prime_number:
# else:
#      list_factor.append(prime_number)
   
# print(list_factor)
