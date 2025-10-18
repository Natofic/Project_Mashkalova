num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

sum_numbers = num1 + num2

result = sum_numbers + 1 \
    if sum_numbers % 5 == 0 \
    else sum_numbers - 2

print(f"Сумма чисел: {sum_numbers}")
print(f"Результат: {result}")