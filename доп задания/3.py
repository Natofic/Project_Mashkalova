number = int(input("Введите двухзначное число: "))

if 10 <= number <= 99:
    digit1 = number // 10
    digit2 = number % 10
    sum_digits = digit1 + digit2

    if sum_digits % 2 == 0:
        result = number + 2
    else:
        result = number - 2

    print(f"Сумма цифр: {sum_digits}")
    print(f"Результат: {result}")
else:
    print("Ошибка: введите двухзначное число!")