
class Hero:

    # конструктор класса НЕ Ф-Я
    def __init__(self, nick_name, lvl, hp):    # self.. - аргументы
        #   атрибуты класса - self.name_hero ...
        self.name_hero = nick_name # ..сам.. = аргументы
        self.lvl = lvl
        self.hp = hp

    #методы класса
    def action(self): # self -
        return f"{self.name_hero} Hi this my base action!"


#   объект/экземпляр класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100,1000)
sinon = Hero("Sinon", 100, 1000)


# вызов
print(f"Nicname: {kirito.name_hero}, lvl: {kirito.lvl}, hp: {kirito.hp}")
print(f"Nicname: {asuna.name_hero}, lvl: {asuna.lvl}, hp: {asuna.hp}")
print(f"Nicname: {sinon.name_hero}, lvl: {sinon.lvl}, hp: {sinon.hp}")

print(kirito.action())
print(asuna.action())
print(sinon.action())






# # функция
# def test(name, age):    #   def test (аргументы)
#     pass
# test("name",12) #   аргументы


