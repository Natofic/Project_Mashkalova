num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

product = num1 * num2

if product < 0:
    result = product * 8
else:
    result = product * 1.5

print(f"Результат: {result}")