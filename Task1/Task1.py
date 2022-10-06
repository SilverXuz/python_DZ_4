"""
Вычислить число c заданной точностью d
Пример:
- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
"""
import math
d = input('Введите точность: ')

d = str(d)
len_d = len(d) - 2
x = math.pi
print(f"pi = {x:.{len_d}f}")
