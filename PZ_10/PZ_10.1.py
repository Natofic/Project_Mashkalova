"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел.
Сформировать новый текстовый файл (.txt) следующего вида, предварительно
выполнив требуемую обработку элементов:

Исходные данные:
Количество элементов:
Индекс последнего максимального элемента:
Меняем местами первую и последнюю трети
"""

numbers = [15, -3, 8, -12, 5, 0, -7, 21, -4, 9, 11, -6, 18, -2, 14, 3, -9, 7, -1, 13]

with open('numbers.txt', 'w', encoding='utf-8') as f:
    for num in numbers:
        f.write(str(num) + ' ')

print()
print("Исходные данные:", numbers)

with open('numbers.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    numbers_list = list(map(int, content.split()))

max_value = max(numbers_list)
last_max_index = -1
for i in range(len(numbers_list)):
    if numbers_list[i] == max_value:
        last_max_index = i

print(f"Количество элементов: {len(numbers_list)}")
print(f"Индекс последнего максимального элемента: {last_max_index}")

n = len(numbers_list)
third_size = n // 3

if third_size > 0:
    first_third = numbers_list[:third_size]
    middle_third = numbers_list[third_size:2 * third_size]
    last_third = numbers_list[2 * third_size:]

    new_numbers = last_third + middle_third + first_third

    print(f"Результат обмена: {new_numbers}")
else:
    new_numbers = numbers_list.copy()
    print("Слишком мало элементов для разделения на трети")

with open('numbers_result.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные:\n")
    f.write(' '.join(map(str, numbers_list)) + '\n')
    f.write(f"Количество элементов: {n}\n")
    f.write(f"Индекс последнего максимального элемента: {last_max_index}\n")
    f.write("Меняем местами первую и последнюю трети:\n")
    f.write(' '.join(map(str, new_numbers)) + '\n')