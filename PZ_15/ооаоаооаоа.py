import sqlite3 as sq
import os
DB_NAME = "study_plan.db"
def create_database():
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Disciplines (
                code INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                specialty TEXT NOT NULL,
                lectures INTEGER DEFAULT 0,
                practices INTEGER DEFAULT 0,
                labs INTEGER DEFAULT 0,
                report_form TEXT DEFAULT 'Экзамен'
            )""")
            print("База данных и таблица созданы.")
    except sq.Error as e:
        print(f"Ошибка при создании БД: {e}")


def insert_initial_data():
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM Disciplines")
            count = cur.fetchone()[0]

            if count == 0:
                data = [
                    ("Высшая математика", "Информационные системы и программирование", 92, 20, 0, "Экзамен"),
                    ("Основы алгоритмизации и программирования", "Информационные системы и программирование", 106, 16, 2, "Экзамен"),
                    ("Основы Web-технологий", "Информационные системы и программирование", 84, 20, 0, "Диф. зачет"),
                ]

                cur.executemany("""INSERT INTO Disciplines 
                                   (name, specialty, lectures, practices, labs, report_form) 
                                   VALUES (?, ?, ?, ?, ?, ?)""", data)
                print("Добавлено 3 начальные записи.")
            else:
                print("База данных уже содержит данные. Пропуск инициализации.")

    except sq.Error as e:
        print(f"Ошибка при добавлении данных: {e}")


def print_all_records():
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Disciplines")
            records = cur.fetchall()

            if not records:
                print("Таблица пуста.")
                return

            print(f"\n{'ID':<5} {'Название':<30} {'Специальность':<25} {'Лек':<5} {'Прак':<5} {'Лаб':<5} {'Отчет':<10}")
            print("-" * 85)

            for row in records:
                print(f"{row[0]:<5} {row[1]:<30} {row[2]:<25} {row[3]:<5} {row[4]:<5} {row[5]:<5} {row[6]:<10}")
            print("-" * 85)

    except sq.Error as e:
        print(f"Ошибка при чтении данных: {e}")

def search_by_specialty(specialty_name):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "SELECT * FROM Disciplines WHERE specialty LIKE ?"
            cur.execute(query, (f"%{specialty_name}%",))
            results = cur.fetchall()

            print(f"\n--- Результат поиска по специальности '{specialty_name}' ---")
            if results:
                for row in results:
                    print(row)
            else:
                print("Ничего не найдено.")
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def search_by_hours(min_lectures):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "SELECT name, lectures FROM Disciplines WHERE lectures > ? ORDER BY lectures DESC"
            cur.execute(query, (min_lectures,))
            results = cur.fetchall()

            print(f"\n--- Дисциплины с лекциями > {min_lectures} ---")
            if results:
                for row in results:
                    print(f"Дисциплина: {row[0]}, Лекций: {row[1]}")
            else:
                print("Ничего не найдено.")
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def search_by_report_form(report_type):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "SELECT * FROM Disciplines WHERE report_form = ?"
            cur.execute(query, (report_type,))
            results = cur.fetchall()

            print(f"\n--- Дисциплины с отчетом '{report_type}' ---")
            if results:
                for row in results:
                    print(f"ID: {row[0]}, Название: {row[1]}")
            else:
                print("Ничего не найдено.")
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def update_add_hours(code, hours_to_add, column_name):
    allowed_columns = ['lectures', 'practices', 'labs']
    if column_name not in allowed_columns:
        print("Ошибка: Неверное название колонки. Используйте lectures, practices или labs.")
        return

    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = f"UPDATE Disciplines SET {column_name} = {column_name} + ? WHERE code = ?"
            cur.execute(query, (hours_to_add, code))

            if cur.rowcount > 0:
                print(f"Успешно обновлено. Добавлено {hours_to_add} ч. в поле '{column_name}' для ID {code}.")
            else:
                print("Запись с таким ID не найдена.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")

def change_report_form(old_form, new_form):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "UPDATE Disciplines SET report_form = ? WHERE report_form = ?"
            cur.execute(query, (new_form, old_form))

            print(f"Изменено записей: {cur.rowcount}. Было '{old_form}', стало '{new_form}'.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")


def rename_discipline(code, new_name):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "UPDATE Disciplines SET name = ? WHERE code = ?"
            cur.execute(query, (new_name, code))

            if cur.rowcount > 0:
                print(f"Название дисциплины ID {code} изменено на '{new_name}'.")
            else:
                print("Запись с таким ID не найдена.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")

def delete_by_code(code):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "DELETE FROM Disciplines WHERE code = ?"
            cur.execute(query, (code,))

            if cur.rowcount > 0:
                print(f"Запись с ID {code} удалена.")
            else:
                print("Запись с таким ID не найдена.")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")


def delete_by_specialty(specialty_name):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "DELETE FROM Disciplines WHERE specialty = ?"
            cur.execute(query, (specialty_name,))

            print(f"Удалено записей специальности '{specialty_name}': {cur.rowcount}.")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")


def delete_low_load_disciplines(max_total_hours):
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            query = "DELETE FROM Disciplines WHERE (lectures + practices + labs) < ?"
            cur.execute(query, (max_total_hours,))

            print(f"Удалено дисциплин с нагрузкой < {max_total_hours} ч.: {cur.rowcount}.")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")


def main():
    print("--- Запуск приложения УЧЕБНЫЙ ПЛАН (Вариант 9) ---")
    create_database()
    insert_initial_data()
    print_all_records()

    print("\n=== ТЕСТИРОВАНИЕ ПОИСКА ===")
    search_by_specialty("Программная инженерия")
    search_by_hours(50)
    search_by_report_form("Зачет")

    print("\n=== ТЕСТИРОВАНИЕ РЕДАКТИРОВАНИЯ ===")
    update_add_hours(1, 10, "lectures")
    change_report_form("Зачет", "Зачет с оценкой")
    rename_discipline(2, "Линейная алгебра и геометрия")

    print("\n--- Данные после редактирования ---")
    print_all_records()

    print("\n=== ТЕСТИРОВАНИЕ УДАЛЕНИЯ ===")
    delete_by_code(8)

    delete_by_specialty("Общие дисциплины")

    delete_low_load_disciplines(50)

    print("\n--- Финальные данные в БД ---")
    print_all_records()

    print("\nПрограмма завершена.")

if __name__ == "__main__":
    main()