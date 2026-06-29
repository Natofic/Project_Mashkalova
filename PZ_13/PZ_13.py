""""
В исходном текстовом файле (Dostoevsky.txt) найти все варианты
фамилии Достоевского (т.е. с различными окончаниями, например,
Достоевский, Достоевского) в единственном экземпляре.
"""
import re
def find_unique_dostoevsky_variants(filename="Dostoevsky.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return []

    pattern = r'Достоевск[а-яА-ЯёЁ]*\b'
    all_matches = re.findall(pattern, text)
    unique_matches = set(all_matches)
    sorted_unique_matches = sorted(list(unique_matches))

    return sorted_unique_matches

if __name__ == "__main__":
    variants = find_unique_dostoevsky_variants()
    if variants:
        print(f"Найдено {len(variants)} уникальных вариантов фамилии:")
        for variant in variants:
            print(f"- {variant}")
    else:
        print("Совпадений не найдено.")