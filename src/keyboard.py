from src.item import Item


class KeyboardLanguage:
    Lang = 'EN'

    def __init__(self):
        self.__lang = self.Lang

    @property
    def language(self):
        return self.__lang

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = 'RU'
        else:
            self.__lang = "EN"
        return self


class Keyboard(Item, KeyboardLanguage):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        KeyboardLanguage.__init__(self)
