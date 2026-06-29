"""
Создайте класс «Книга», который имеет атрибуты название, автор и количество страниц.
Добавьте методы для чтения и записи книги.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.content = [""] * pages
        self.current_page = 0

    def write_page(self, page_num, text):
        if 0 <= page_num < self.pages:
            self.content[page_num] = text
        else:
            raise ValueError("Неверный номер страницы")

    def read_page(self, page_num=None):
        page = page_num if page_num is not None else self.current_page
        if 0 <= page < self.pages:
            self.current_page = page
            return self.content[page]
        raise ValueError("Страница не существует")

    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} стр."

if __name__ == "__main__":
    book = Book("Какая-то книга", "Машкалова", 3)
    book.write_page(0, "Intro")
    book.write_page(1, "Basics")
    book.write_page(2, "Advanced")
    print(book.get_info())
    print("Page 1:", book.read_page(0))
    print("Current:", book.read_page())