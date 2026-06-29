# Задача 1
def task1():
    try:
        count_negative = 0
        sum_negative = 0

        for i in range(4):
            num = int(input(f"Введите число {i + 1}: "))
            if num < 0:
                count_negative += 1
                sum_negative += num

        print(f"Количество отрицательных чисел: {count_negative}")
        print(f"Сумма отрицательных чисел: {sum_negative}")

    except ValueError:
        print("Ошибка: Введите числа корректно!")


# Задача 2
def task2():
    try:
        count_even = 0

        for i in range(4):
            num = int(input(f"Введите целое число {i + 1}: "))
            if num % 2 == 0:
                count_even += 1

        print(f"Количество четных чисел: {count_even}")

    except ValueError:
        print("Ошибка: Введите целые числа!")


# Задача 3
def task3():
    try:
        print("Число\tКвадрат\tКуб")
        for i in range(2, 6):
            print(f"{i}\t{i ** 2}\t{i ** 3}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Задача 4
def task4():
    try:
        n = int(input("Введите n (n > 1): "))
        if n <= 1:
            raise ValueError("n должно быть больше 1")

        total_sum = 0
        factorial = 1

        for i in range(1, n + 1):
            factorial *= i
            total_sum += factorial

        print(f"S = {total_sum}")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Задача 5
def task5():
    try:
        n = int(input("Введите количество чисел N: "))
        if n <= 0:
            raise ValueError("N должно быть больше 0")

        total = 0
        for i in range(n):
            num = int(input(f"Введите число {i + 1}: "))
            total += num

        average = total / n
        print(f"Среднее арифметическое: {average:.2f}")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Задача 6
def task6():
    try:
        n = int(input("Введите количество чисел N: "))
        if n <= 0:
            raise ValueError("N должно быть больше 0")

        count_zero = 0
        for i in range(n):
            num = int(input(f"Введите число {i + 1}: "))
            if num == 0:
                count_zero += 1

        print(f"Количество чисел равных нулю: {count_zero}")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Задача 7
def task7():
    try:
        A = int(input("Введите целое число A: "))
        B = int(input("Введите целое число B (B > A): "))

        if A >= B:
            raise ValueError("A должно быть меньше B")

        numbers = []
        for i in range(B, A - 1, -1):
            numbers.append(i)

        print("Числа в порядке убывания:", *numbers)
        print(f"Количество чисел: {len(numbers)}")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Задача 8
def task8():
    try:
        A = int(input("Введите целое число A: "))
        B = int(input("Введите целое число B (B > A): "))

        if A >= B:
            raise ValueError("A должно быть меньше B")

        total_sum = 0
        for i in range(A, B + 1):
            total_sum += i

        print(f"Сумма чисел от {A} до {B}: {total_sum}")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Задача 9
def task9():
    try:
        a1 = int(input("Введите первый член прогрессии: "))
        d = int(input("Введите разность прогрессии: "))
        n = int(input("Введите количество членов: "))

        if n <= 0:
            raise ValueError("Количество членов должно быть больше 0")

        count = 0
        for i in range(n):
            term = a1 + i * d
            if 10 < term < 30:
                count += 1

        print(f"Количество элементов, удовлетворяющих условию: {count}")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Задача 10
def task10():
    try:
        N = int(input("Введите N (N ≥ 3): "))
        if N < 3:
            raise ValueError("N должно быть не меньше 3")

        fib = [0, 1]
        even_count = 0

        for i in range(2, N):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
            if next_fib % 2 == 0:
                even_count += 1

        print(f"Первые {N} чисел Фибоначчи: {fib}")
        print(f"Количество четных чисел: {even_count}")

    except ValueError as e:
        print(f"Ошибка: {e}")


# Задача 11
def task11():
    try:
        n = int(input("Введите количество элементов прогрессии: "))
        if n <= 0:
            raise ValueError("Количество элементов должно быть больше 0")

        a = 1
        results = []

        for i in range(n):
            divided = a / 2
            rounded = round(divided)
            results.append(rounded)
            print(f"a{i + 1} = {a} -> {a}/2 = {divided} -> округлено: {rounded}")
            a += 3

        print("\nРезультаты:", results)

    except ValueError as e:
        print(f"Ошибка: {e}")



def main():
    tasks = {
        1: task1, 2: task2, 3: task3, 4: task4, 5: task5,
        6: task6, 7: task7, 8: task8, 9: task9, 10: task10, 11: task11
    }

    try:
        choice = int(input("Введите номер задачи (1-11): "))
        if choice not in tasks:
            print("Ошибка: Введите число от 1 до 11")
        else:
            tasks[choice]()
    except ValueError:
        print("Ошибка: Введите целое число!")


if __name__ == "__main__":
    main()