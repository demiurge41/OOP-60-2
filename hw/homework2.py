# Постановка задачи
# Что нужно сделать это создать две директории (lessons, hw)
# где будите хранить код уроков и код ДЗ. Создайте небольшую иерархию классов,
# моделирующую животных в «волшебном зоопарке». У каждого животного есть базовые
# характеристики и уникальная суперспособность, которую оно может использовать.
from codecs import replace_errors


# 1) Базовый класс Animal
# 2) Миксины(mix - in) – отдельные способности, не зависящие от типа животного:
#
#     -Flyable – умеет летать
#     -Swimmable – умеет плавать
#     -Invisible – умеет становиться невидимым
#
# Каждый миксин переопределяет use_ability и вызывает super().use_ability()
# (чтобысобрать все способностив одну строку).
#

class Animal:
    def __init__(self, name: str):
       self.name = name

    def info(self):
        return self.name

    def use_ability(self):
        return "Has no special abilities."


"""---"""
class Flyable:
    def use_ability(self):
        return super().use_ability() + " + FLY "

class Swimmable:
    def use_ability(self):
        return super().use_ability() + " + SWIMM "

class Invisible:
    def use_ability(self):
        return super().use_ability() + " + INVIS "


"""---"""
class Duck(Swimmable, Flyable, Animal):
    def use_ability(self):
        return  f"{super().use_ability()} - ( Duck )"

"""---"""
class Bat(Flyable, Animal):
    def use_ability(self):
        return  f"{super().use_ability()} - ( Bat )"

"""---"""
class Frog(Swimmable, Invisible, Animal):
    def use_ability(self):
        return  f"{super().use_ability()} - ( Frog )"

"""---"""
class Phoenix(Flyable, Animal):
    def use_ability(self):
        return  f"{super().use_ability()} - ( Phoenix )"


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
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_all(self):
        for animal in self.animals:
            print(animal.info())

    def perform_show(self):
        for animal in self.animals:
            print(f"{animal.name}: {animal.use_ability()}")

zoo = Zoo()
zoo.add_animal(Duck("Zigzag McQuack"))
zoo.add_animal(Bat("Bruce Wayne"))
zoo.add_animal(Frog("Tsarevna Lyagushka"))
zoo.add_animal(Phoenix("Skyress Ventus"))

print("Animals in ZOO: ")
zoo.show_all()
print("Animal show: ")
zoo.perform_show()