"""
Даны целые положительные числа А и B (А > В).
На отрезке длины А размещено максимально возможное количество отрезков алины в (без наложений).
Используя операцию деления нацело, найти количество отрезков В, размещенных на отрезке А.
"""

def calculate_segments(A, B):
    if not (isinstance(A, int) and isinstance(B, int)):
        raise TypeError
    if not (A > 0 and B > 0):
        raise TypeError
    if (A > B):
        return A // B
    if not (A > B):
        raise ValueError

try:
    А = int(input("Введите целое положительное число А:"))
    B = int(input("Введите целое положительное число В:"))
    result = calculate_segments(А,B)
    print (f"На отрезке ДЛИНЫ {А} можно разместить {result} отрезков длины {B}")
except ValueError:
    print (f"Ошибка: Введите целые числа, где А > В")
except TypeError:
    print(f"Ошибка: Введите целые положительные числа")