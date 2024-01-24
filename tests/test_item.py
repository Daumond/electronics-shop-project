"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
from src.phone import Phone
import pytest


@pytest.fixture
def item():
    item = Item("Laptop", 5000, 3)
    return item


def test_init(item):
    assert item.name == "Laptop"
    assert item.price == 5000
    assert item.quantity == 3


def test_repr(item):
    assert repr(item) == "Item('Laptop', 5000, 3)"


def test_str(item):
    assert str(item) == "Laptop"


def test_calculate_total_price():
    item = Item("Laptop", 5000, 3)
    assert item.calculate_total_price() == 15000


def test_apply_discount():
    item = Item("Laptop", 5000, 3)
    item.pay_rate = 0.8
    assert item.apply_discount() is None
    item.apply_discount()
    assert item.price == 3200.0


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('abc') == 'abc'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_if_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        Item.instantiate_from_csv("../tests/file")  # Несуществующий файл
    assert "Отсутствует файл item.csv" in str(excinfo)


corrupted_file_path = "../tests/test_items_corrupted.csv"  # Специально измененный файл


def test_if_file_is_corrupted():
    with pytest.raises(InstantiateCSVError) as excinfo:
        Item.instantiate_from_csv(corrupted_file_path)
    assert "Файл item.csv поврежден" in str(excinfo)
