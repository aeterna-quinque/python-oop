from abc import ABC, abstractmethod


class Pizza(ABC):
    """

    Абстрактный класс для пиццы.

    """

    @abstractmethod
    def __init__(self):
        self.__size = ""
        self.__dough = ""
        self.__sauce = ""
        self.__ingredients = {}
        self.__prices = {}
        self.__name = ""
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def dough(self):
        return self.__dough

    @property
    def sauce(self):
        return self.__sauce

    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def prices(self):
        return self.__prices

    @size.setter
    def size(self, value):
        self.__size = value
        self.price = value

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @sauce.setter
    def sauce(self, value):
        self.__sauce = value

    @ingredients.setter
    def ingredients(self, values: dict):
        self.__ingredients = values

    @name.setter
    def name(self, value):
        self.__name = value

    @price.setter
    def price(self, value):
        self.__price = self.__prices[value]

    @prices.setter
    def prices(self, values):
        self.__prices = values


class Barbecue(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Barbecue"


class Pepperoni(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Pepperoni"


class Seafood(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Seafood"
