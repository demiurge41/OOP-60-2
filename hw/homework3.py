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
   def get_service(self):
       return f"Сервис: {self._service}"


class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"

    def send(self, message, recipient):
        return f"Email sent to {recipient}"

class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    def send(self, message, recipient):
        return f"SMS sent to {recipient}"

class PushSender(NotificationSender):

    def __init__(self):
        self._service = "Firebase"

    def send(self, message, recipient):
        return f"Push sent to {recipient}"

email = EmailSender()
print(email.send("Привет", "zara@gmail.com"))
print(email.get_service())

sms = SmsSender()
print(sms.send("сообщение1236", "+996123456789"))
print(sms.get_service())

push = PushSender()
print(push.send("пуш уведомление","akk1"))
print(push.get_service())


"""Задание 3"""

class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier

    def login(self, password):
        res = self.account.get_balance(password)
        if res == "Неверный пароль!":
            return False

        self.notifier.send(f"Успешный вход: {self.username}", "+996123456789")
        return True

    def transfer(self, amount, password, recipient_account: BankAccount):
        res = self.account.withdraw(amount, password)
        if res == "Неверный пароль!":
            print("Неверный пароль!")
            return False
        if res == "Недостаточно стредств!":
            print("Недостаточно средств!")
            return False

        recipient_account._balance += amount

        self.notifier.send(f"Перевод {amount} отправлен", "+996123456789")
        self.notifier.send(f"Получено {amount} от {self.username}", "+996123456789")

        print(f"перевод успешен +{amount}. Баланс: {res}.")
        return True

zara = BankAccount("Zara", 2000, "secret")
aisha = BankAccount("Aisha", 300, "pass123")
notifier = SmsSender()
auth = UserAuth("Aisha_doe", aisha, notifier)
auth.login("secret")
auth.transfer(90, "secret", aisha)

print(zara._balance)
print(aisha._balance)





