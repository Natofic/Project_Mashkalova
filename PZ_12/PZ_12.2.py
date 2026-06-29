"""
В матрице найти среднее арифметическое положительных элементов, кратных 3.
"""

import random

rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

print("\nМатрица:")
[print(i) for i in matrix]

elements = [elem for i in matrix for elem in i if elem > 0 and elem % 3 == 0]
mean_value = sum(elements) / len(elements) if elements else 0

print(f"\nПоложительные элементы, кратные 3: {elements}")
print(f"Среднее арифметическое: {mean_value:.2f}")