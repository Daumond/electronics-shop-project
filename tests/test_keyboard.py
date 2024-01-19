import pytest

from src.keyboard import Keyboard

def test_name():

    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

def test_change_lang():

    kb = Keyboard('Dark Project KD87A', 9600, 5)

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"