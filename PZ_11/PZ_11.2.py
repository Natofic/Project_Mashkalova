"""
Из заданной строки отобразить только символы нижнего регистра.
Использовать библиотеку string. Строка 'In PyCharm, you can specify
third-party standalone applications and run them as External Tools
"""

import string

text = "In PyCharm, you can specify third-party standalone applications and run them as External Tools"

result = ""

for char in text:
    if char not in string.ascii_lowercase:
        result += char

print("Результат:", result)