# Постановка задачи
# Что нужно сделать это создать две директории (lessons, hw)
# где будите хранить код уроков и код ДЗ. Создайте небольшую иерархию классов,
# моделирующую животных в «волшебном зоопарке». У каждого животного есть базовые
# характеристики и уникальная суперспособность, которую оно может использовать.

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
    def __init__(self, animal: str):
        self.animal = ["Duck, Bat, Frog, Phoenix"]




class Animal:
   def __init__(self, name: str, age: int, health: int):
       self.name = name
       self.age = age
       self.health = health      # очки здоровья

   def info(self) -> str:
       return f"{self.name}, {self.age} age, HP {self.health}"

   def use_ability(self) -> str:
       """Переопределяется в наследниках"""
       return f"{self.name} uses a basic ability."









