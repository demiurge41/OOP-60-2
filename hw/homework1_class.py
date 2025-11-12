# Создай свой собственный класс (например, Car, Animal, Student, GameCharacter — любой на твой выбор).
#   Условия:
# 1 Класс должен иметь 3 атрибута (например: name, age, speed).
# 2 Класс должен иметь 2 метода:
#- один метод — пусть возвращает строку с описанием объекта,
#- второй метод — выполняет какое-нибудь простое действие (например, увеличивает скорость, меняет настроение и т.п.).
# 3 Создай 2 объекта (экземпляра) этого класса с разными значениями атрибутов.
# 4 Вызови методы у этих объектов и выведи результат в консоль с помощью print().
# 5 GIT. нужно будет залить это все на ваш репозиторый, и прикрепить ссылку на ваш репозиторий

class GameCharacter:

    def __init__(self, nickname, race_type, class_type):
        self.nickname = nickname
        self.race_type = race_type
        self.class_type = class_type
        self.speed = 10

    def description(self):
        return (f"Имя: {self.nickname}\n"
                f"Раса: {self.race_type}\n"
                f"Класс: {self.class_type}\n"
                f"Скорость: {self.speed}"

                )

    def class_speed(self):
        self.speed += 5
        return f"Скорость +5[{self.speed}]"

nurik = GameCharacter("Nurik", "lizard", "fighter")
deidara = GameCharacter("Deidara", "hunam", "mage")

print(nurik.description())
print(nurik.class_speed())
print()
print(deidara.description())
print(deidara.class_speed())






    # def races_description(self):
    #     if self.race_type == "elf":
    #         return "Elves are graceful yet fierce beings deeply connected to nature and memory."
    #     elif self.race_type == "dwarf":
    #         return "Dwarves are stalwart warriors renowned for their resilience and strength."
    #     elif self.race_type == "lizard":
    #         return "Lizards are an ancient and mystical race, distinguished by their natural affinity for magic and intellectual prowess."
    #     elif self.race_type == "human":
    #         return "Humans are a versatile and balanced race, ideal for players seeking flexibility in their gameplay."
    #     else:
    #         return "Unknown race."

    # def class_speed(self):
    #     if self.class_type == "cleric":
    #         self.speed += 5
    #         return f"{self.class_type.upper()}. Speed +5 [{self.speed}]."
    #     elif self.class_type == "fighter":
    #         self.speed += 7
    #         return f"{self.class_type.upper()}. Speed +7 [{self.speed}].."
    #     elif self.class_type == "mage":
    #         self.speed += 4
    #         return f"{self.class_type.upper()}. Speed +4  [{self.speed}].."
    #     elif self.class_type == "ranger":
    #         self.speed += 10
    #         return f"{self.class_type.upper()}. Speed +10 [{self.speed}].."
    #     else:
    #         return "Unknown class."