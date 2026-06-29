def sum_of_digits(number):
    total = 0
    n = abs(number)

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total


def task1():
    print("Задача 1")

    num1 = int(input("Введите первое целое число: "))
    num2 = int(input("Введите второе целое число: "))
    num3 = int(input("Введите третье целое число: "))

    sum1 = sum_of_digits(num1)
    sum2 = sum_of_digits(num2)
    sum3 = sum_of_digits(num3)

    print(f"\nСумма цифр числа {num1} = {sum1}")
    print(f"Сумма цифр числа {num2} = {sum2}")
    print(f"Сумма цифр числа {num3} = {sum3}")

    if sum1 > sum2 and sum1 > sum3:
        print(f"Наибольшая сумма цифр у числа {num1}")
    elif sum2 > sum1 and sum2 > sum3:
        print(f"Наибольшая сумма цифр у числа {num2}")
    elif sum3 > sum1 and sum3 > sum2:
        print(f"Наибольшая сумма цифр у числа {num3}")
    else:
        print("У нескольких чисел одинаковая наибольшая сумма цифр")


def calculate_perimeter(length, width):
    return 2 * (length + width)


def calculate_area(length, width):
    return length * width


def task2():
    print("\nЗадача 2")

    length = int(input("Введите длину прямоугольника: "))
    width = int(input("Введите ширину прямоугольника: "))

    while length <= 0 or width <= 0:
        print("Длина и ширина должны быть положительными числами!")
        length = int(input("Введите длину прямоугольника: "))
        width = int(input("Введите ширину прямоугольника: "))

    perimeter = calculate_perimeter(length, width)
    area = calculate_area(length, width)

    print(f"\nПериметр прямоугольника: {perimeter}")
    print(f"Площадь прямоугольника: {area}")


def count_digits(number):
    if number == 0:
        return 1

    count = 0
    n = abs(number)

    while n > 0:
        count += 1
        n = n // 10

    return count


def task3():
    print("\nЗадача 3")
    number = int(input("Введите целое число: "))
    digit_count = count_digits(number)
    print(f"Количество цифр в числе {number}: {digit_count}")


def main():
    tasks = {
        1: task1, 2: task2, 3: task3,
        }

    try:
        choice = int(input("Введите номер задачи (1-3): "))
        if choice not in tasks:
            print("Ошибка: Введите число от 1 до 3")
        else:
            tasks[choice]()
    except ValueError:
        print("Ошибка: Введите целое число!")


if __name__ == "__main__":
    main()