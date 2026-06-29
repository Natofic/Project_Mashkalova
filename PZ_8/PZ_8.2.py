"""
Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние
температуры по месяцам в году. Преобразовать информацию из строки в словарь, с
использованием функции найти среднюю и минимальные температуры, результаты
вывести на экран.
"""

temperatures_str = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

parts = []
current = ""
for char in temperatures_str + " ":
    if char != " ":
        current += char
    elif current:
        parts.append(current)
        current = ""

year = parts[0]
temps = [int(x) for x in parts[1:]]

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

temperatures_dict = {months[i]: temps[i] for i in range(12)}

avg_temp = sum(temps) / len(temps)
min_temp = min(temps)
min_month = months[temps.index(min_temp)]

print(f"\nРезультаты анализа за {year}:")
print(f"Средняя температура за год: {avg_temp:.2f}°C")
print(f"Минимальная температура: {min_temp}°C в {min_month}")

print("Температуры по месяцам в виде таблицы:")
print(f"{'Месяц':<12} {'Температура':<12}")

for month, temp in temperatures_dict.items():
    print(f"{month:<12} {temp:>4}°C")