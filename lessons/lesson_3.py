# инкапсуляция
# import random
# import string
#
# class BankAccount:
#     def __init__(self, name, balance, password):
#         self.name = name # открытая
#         self._balance = balance # '_' - защищеный атрибут
#         self.__password = password # "__" - приватная атрибута
#
#     def login(self, password):
#         if self.__password == password:
#             print("Вы вошли!!")
#         else:
#             print("Неверный пароль!")
#
#     def get_balance(self, password):
#         if self.__password == password:
#             return self._balance
#         else:
#             return "Неверный пароль!"
#
#     def __random_pass(self):
#         chart = string.ascii_letters + string.digits
#         password = ''.join(random.choice(chart) for _ in range(6))
#         return password
#
#     def get_new_pass(self):
#         return self.__random_pass()
#
# john = BankAccount("John", 100, "123qwerty")
#
# print(john.__dict__)
# print(john._BankAccount__password)
#
# john.login("123321")
# print(john.get_balance("123qwerty"))
# print(john.get_new_pass())






# абстракция

from abc import ABC, abstractmethod
# абстрактный класс
class Animal(ABC):
    def make_sound(self):
        pass

    def move(self):
        pass

class Dog(Animal):

    def make_sound(self):
        return "gaf gaf"

    def move(self):
        return "step"

# gufi = Dog()
# print(gufi.make_sound())

class SmsSend(ABC):
    @abstractmethod
    def send_otp(self):
        pass

class KgSms(SmsSend):

    def send_otp(self):

        text = "<text>1234</text>"
        phone = "<phone>+996779</phone>"

        self.send(text, phone)

class RuSms(SmsSend):

    def send_otp(self):
        data = {
            "text": "1234",
            "phone": "+7924"
        }
        self.send_sms(data)

