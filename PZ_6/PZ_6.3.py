"""
Дано множество A из N точек на плоскости и точка B
(точки заданы своими координатами x, y). Найти точку
из множества A, наиболее близкую к точке B.
Расстояние R между точками с координатами (x₁, y₁) и (x₂, y₂) вычисляется по формуле:

R = \sqrt{(x₂ - x₁)^2 + (y₂ - y₁)^2}.

Для хранения данных о каждом наборе точек следует
использовать по два списка: первый список для хранения абсцисс,
второй — для хранения ординат.
"""

import random
import math


def main():
    N = random.randint(3, 8)
    x_list = [random.uniform(-10, 10) for _ in range(N)]
    y_list = [random.uniform(-10, 10) for _ in range(N)]

    Bx = random.uniform(-10, 10)
    By = random.uniform(-10, 10)

    print("Множество A (индекс: (x, y)):")
    for i in range(N):
        print(f"{i}: ({x_list[i]:.2f}, {y_list[i]:.2f})")
    print(f"Точка B: ({Bx:.2f}, {By:.2f})")

    min_dist = float('inf')
    min_index = -1
    for i in range(N):
        dx = x_list[i] - Bx
        dy = y_list[i] - By
        dist = math.sqrt(dx * dx + dy * dy)
        if dist < min_dist:
            min_dist = dist
            min_index = i

    print("Ближайшая точка из A к B:")
    print(f"Индекс: {min_index}")
    print(f"Координаты: ({x_list[min_index]:.2f}, {y_list[min_index]:.2f})")
    print(f"Расстояние: {min_dist:.2f}")

main()