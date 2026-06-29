"""
Даны две последовательности. Найти элементы,
общие для двух последовательностей и их количество.
"""

import random

length = 5

a = [random.randint(0, 20) for _ in range(length)]
b = [random.randint(0, 20) for _ in range(length)]

print("Первая последовательность:", a)
print("Вторая последовательность:", b)

common = list(set(a) & set(b))

print("Общие элементы:", common)
print("Количество общих элементов:", len(common))