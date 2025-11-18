# Постановка задачи
# Что нужно сделать это создать две директории (lessons, hw)
# где будите хранить код уроков и код ДЗ. Создайте небольшую иерархию классов,
# моделирующую животных в «волшебном зоопарке». У каждого животного есть базовые
# характеристики и уникальная суперспособность, которую оно может использовать.
from codecs import replace_errors


# 1) Базовый класс Animal
# 2) Миксины(mix - in) – отдельные способности, не зависящие от типа животного:
#     -Flyable – умеет летать
#     -Swimmable – умеет плавать
#     -Invisible – умеет становиться невидимым
# Каждый миксин переопределяет use_ability и вызывает super().use_ability()
# (чтобысобрать все способностив одну строку).


class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health

    def info(self):
        return f"{self.name}, {self.age} лет, здоровье {self.health}"

    def use_ability(self):
        return "Использует базовую способность."


"""---"""
class Flyable:
    def use_ability(self):
        return super().use_ability() + " + летает."

class Swimmable:
    def use_ability(self):
        return super().use_ability() + " + плавает."

class Invisible:
    def use_ability(self):
        return super().use_ability() + " + становится невидимым "


"""---"""
class Duck(Flyable, Swimmable, Animal):
    pass

class Bat(Flyable, Animal):
    pass

class Frog(Swimmable, Invisible, Animal):
    pass

class Phoenix(Flyable, Invisible, Animal):
    pass

# 3) Конкретные животные (наследуют Animal и нужные миксины):
# Duck, Bat, Frog, Phoenix
#
# 4) Класс Zoo
# Хранит список животных (self.animals: list[Animal]).
#     Методы
#         -add_animal(animal: Animal)
#         -show_all() – печатает info() каждого животного
#         -perform_show() – каждое животное вызывает use_ability() и выводит результат



# 4)
class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_all(self):
        for animal in self.animals:
            print(animal.info())

    def perform_show(self):
        for animal in self.animals:
            print(f"{animal.name}: {animal.use_ability()}")

if __name__ == "__main__":
    zoo = Zoo()

    duck = Duck("Zigzag McQuack", 4, 90)
    bat = Bat("Bruce Wayne", 2, 100)
    frog = Frog("Tsarevna Lyagushka", 5,200)
    phoenix = Phoenix("Skyress Ventus", 9, 500)

    for animal in (duck, bat, frog, phoenix):
            zoo.add_animal(animal)
print("Информация о животных")
zoo.show_all()
print("\nШоу суперспособностей")
zoo.perform_show()

print("\nMRO для Duck:", Duck.__mro__)
print("MRO для Bat:", Bat.__mro__)
print("MRO для Frog:", Frog.__mro__)
print("MRO для Phoenix:", Phoenix.__mro__)