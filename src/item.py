import csv
import os
from math import floor


class InstantiateCSVError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать с другими классами")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price

    @classmethod
    def instantiate_from_csv(cls, filepath='../src/items.csv'):
        """
        Создаёт экземпляры класса из файла csv
        :param filepath: путь к файлу csv с информацией о конкретных товарах в магазине
        """
        cls.all.clear()
        try:
            with open(os.path.join(filepath), encoding="windows-1251") as file:
                data = [row for row in csv.DictReader(file)]
            for dict_ in data:
                name_, price_, quantity_ = [cls.string_to_number(el) for el in dict_.values()]
                cls(name_, price_, quantity_)
        except ValueError:
            raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(value: str) -> str or int:
        """
        Принимает строку и возвращает int или str в зависимости от типа данных.
        :param value: Строка с информацией, тип данных которой нужно преобразовать
        """
        try:
            number = floor(float(value))
            return number
        except ValueError:
            return value
