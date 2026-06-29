"""
Создайте класс "Фрукт", который содержит информацию о наименовании и весе фрукта.
Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса "Фрукт" и содержат информацию о цвете.
"""
"""ПЗ №16, Блок 2, Вариант 16: Наследование классов Фрукт, Яблоко, Апельсин."""

class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.weight}г"
1
class Apple(Fruit):
    def __init__(self, weight, color):
        super().__init__("Яблоко", weight)
        self.color = color

    def get_info(self):
        return f"Яблоко ({self.color}): {self.weight}г"

class Orange(Fruit):
    def __init__(self, weight, color):
        super().__init__("Апельсин", weight)
        self.color = color

    def get_info(self):
        return f"Апельсин ({self.color}): {self.weight}г"

if __name__ == "__main__":
    fruits = [
        Fruit("Груша", 150),
        Apple(120, "красное"),
        Orange(180, "оранжевый")
    ]
    for f in fruits:
        print(f.get_info())