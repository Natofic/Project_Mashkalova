 # """
 # Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
 # количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
 # в стихотворной форме предварительно поставив последнюю строку фразой введенной
 # пользователем.
 # """

file = open('text18-9.txt', 'r')
poem_text = file.read()
file.close()

with open('text18-9.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("\nСодержимое исходного файла:")
for line in lines:
    print(line.rstrip())

lowercase_count = 0
all_text = ''.join(lines)

for char in all_text:
    if char.isalpha() and char.islower():
        lowercase_count += 1

print(f"Количество букв в нижнем регистре: {lowercase_count}")

uppercase_count = 0
for char in all_text:
    if char.isalpha() and char.isupper():
        uppercase_count += 1

print(f"Количество букв в верхнем регистре: {uppercase_count}")
print(f"Общее количество букв: {uppercase_count + lowercase_count}")

user_phrase = input("Введите фразу для последней строки стихотворения: ")

with open('poem_result.txt', 'w', encoding='utf-8') as f:
    for i in range(len(lines) - 1):
        f.write(lines[i].rstrip() + '\n')

    f.write(user_phrase + '\n')

print("Создан файл 'poem_result.txt' с измененной последней строкой")

print("\nИтоговое стихотворение:")
with open('poem_result.txt', 'r', encoding='utf-8') as f:
    print(f.read())