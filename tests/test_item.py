"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test___init__():
    item = Item("Laptop", 5000, 3)
    assert item.name == "Laptop"
    assert item.price == 5000
    assert item.quantity == 3

def test_calculate_total_price():
    item = Item("Laptop", 5000, 3)
    assert item.calculate_total_price() == 15000

def test_apply_discount():
    item = Item("Laptop", 5000, 3)
    item.pay_rate = 0.8
    assert item.apply_discount() is None
    item.apply_discount()
    assert item.price == 3200.0
