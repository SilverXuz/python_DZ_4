"""
Вычислить число ПИ c заданной точностью d
Пример:
- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
"""
import math
d = input('Введите точность: ')

len_d = len(d) - 2
print(f"pi = {math.pi:.{len_d}f}")
