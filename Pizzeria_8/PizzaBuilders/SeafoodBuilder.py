from Pizzeria_8.Builder import Builder
from Pizzeria_8.Pizza import Seafood


class SeafoodBuilder(Builder):
    """

    Класс Строителя для пиццы Seafood.

    """
    __ingredients = {'prawns': 2, 'mozzarella': 2, 'squid': 2, 'tuna': 2, 'tomatoes': 2}
    __prices = {'small': 450, 'middle': 600, 'large': 750}
    __sauces = ['classic', 'bechamel', 'pesto']

    def __init__(self) -> None:
        self.__pizza = Seafood()
        self.reset()

    def reset(self) -> None:
        self.__pizza = Seafood()
        self.__pizza.dough = "classic"
        self.__pizza.sauce = self.__sauces[0]
        self.__pizza.prices = self.__prices
        self.__pizza.ingredients = self.__ingredients

    @property
    def pizza(self) -> Seafood:
        pizza = self.__pizza
        self.reset()
        return pizza

    @property
    def get_ingredients(self):
        return self.__ingredients.copy()

    @property
    def get_sauces(self):
        return self.__sauces.copy()

    def set_size(self, value) -> None:
        self.__pizza.size = value

    def set_dough(self, value) -> None:
        self.__pizza.dough = value

    def set_sauce(self, value) -> None:
        self.__pizza.sauce = value

    def set_ingredients(self, value) -> None:
        self.__pizza.ingredients = value.copy()

    def get_certain_price(self, size):
        return self.__prices[size]
