import random
import string

"""Задание 1"""

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name # открытая
        self._balance = balance # '_' - защищеный атрибут
        self.__password = password # "__" - приватная атрибута

    def deposit(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"

        if amount <= 0:
            return "Сумма должна быть положительная"

        self._balance += amount
        return self._balance

    def withdraw(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"

        if amount <= 0:
            return "Сумма должна быть положительная"

        if amount > self._balance:
            return "Не хватает средств!"

        self._balance -= amount
        return self._balance

    def change_password(self, old_pass, new_pass):
        if self.__password != old_pass:
            return "Старый пароль неверный!"

        self.__password = new_pass
        return "Пароль изменен"

    def get_balance(self, password):
        if  password != self.__password:
            return "Неверный пароль!"
        return self._balance

    def reset_pin(self, password):
        if password != self.__password:
            return "Неверный пароль!"
        new_pin = self.__generate_pin()
        self.__password = new_pin
        return new_pin

    def __generate_pin(self):
        password = ''.join(random.choice(string.digits) for _ in range(4))
        return password

zara = BankAccount("Zara", 100, "123qwer")

print(zara.deposit(50, "123qwer"))
print(zara.withdraw(200, "123qwer"))
print(zara.get_balance("123qwer"))
print(zara.change_password("false", "321rewq"))
print(zara.reset_pin("123qwer"))
print(zara.get_balance("4567"))

"""Задание 2"""

from abc import ABC, abstractmethod

class NotificationSender(ABC):
   @abstractmethod
   def send(self, message, recipient):
       pass




