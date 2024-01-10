"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def test___init__():
    item = Item("Laptop", 5000, 3)
    return item


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

