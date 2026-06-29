"""
Дан список размера N. Найти количество участков,
на которых его элементы монотонно убывают.
"""

import random


def main():
    N = random.randint(5, 15)
    list = [random.randint(1, 50) for _ in range(N)]
    print("Список размера", N, ":", list)

    count = 0
    in_decrease = False
    for i in range(1, N):
        if list[i] < list[i - 1]:
            if not in_decrease:
                count += 1
                in_decrease = True
        else:
            in_decrease = False

    print("Количество участков монотонного убывания:", count)

main()