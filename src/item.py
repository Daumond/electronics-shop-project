import csv
import os
from math import floor


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

    @property
    def pay_rate(self) -> float:
        return self._pay_rate

    @pay_rate.setter
    def pay_rate(self, pay_rate) -> None:
        self._pay_rate = pay_rate

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
    def instantiate_from_csv(cls, filepath):
        """
        Создаёт экземпляры класса из файла csv
        :param filepath: путь к файлу csv с информацией о конкретных товарах в магазине
        """
        cls.all.clear()
        with open(os.path.join(filepath), encoding="windows-1251") as file:
            data = [row for row in csv.DictReader(file)]
        for dict_ in data:
            name_, price_, quantity_ = [cls.string_to_number(el) for el in dict_.values()]
            cls(name_, price_, quantity_)

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
