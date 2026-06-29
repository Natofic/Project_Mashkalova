"""
Составить программу, в которой функция генерирует четырехзначное число
и определяет, есть ли в числе одинаковые цифры.
"""

import random

def generate_and_check():
    number = random.randint(1000, 9999)
    print(f"Сгенерированное число: {number}")

    temp = number
    digits = []

    while temp > 0:
        digit = temp % 10
        digits.append(digit)
        temp = temp // 10

    i = 0
    has_duplicates = False

    while i < len(digits):
        j = i + 1
        while j < len(digits):
            if digits[i] == digits[j]:
                has_duplicates = True
                break
            j += 1
        if has_duplicates:
            break
        i += 1

    if has_duplicates:
        print("В числе есть одинаковые цифры")
    else:
        print("Все цифры в числе различны")

    return number, has_duplicates

if __name__ == "__main__":
    print("Задача 1")
    generate_and_check()