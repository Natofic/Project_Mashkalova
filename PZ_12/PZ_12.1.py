"""
В матрице элементы второго столбца заменить элементами
из одномерного динамического массива соответствующей размерности.
"""

import random

rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

print(f"\nВведите {rows} чисел для одномерного массива:")
array_1d = list(map(int, input().split()))

print("\nИсходная матрица:")
[print(a) for a in matrix]
print(f"Одномерный массив: {array_1d}")

new_matrix = [[a[j] if j != 1 else array_1d[i] for j in range(len(a))] for i, a in enumerate(matrix)]

print("\nРезультат:")
[print(a) for a in new_matrix]