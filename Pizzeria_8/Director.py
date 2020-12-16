from .Builder import Builder
from .PizzaBuilders.BarbecueBuilder import BarbecueBuilder
from .PizzaBuilders.PepperoniBuilder import PepperoniBuilder
from .PizzaBuilders.SeafoodBuilder import SeafoodBuilder

class Director:
    """

    Класс Директора.
    Отвечает за выполнение шагов создания пиццы в определенной последовательности согласно требованиям клиента.

    """

    def __init__(self) -> None:
        self.__builder = None

    @property
    def builder(self) -> Builder:
        return self.__builder

    @builder.setter
    def builder(self, pizza) -> None:
        if pizza == "Barbecue":
            self.__builder = BarbecueBuilder()
        elif pizza == "Pepperoni":
            self.__builder = PepperoniBuilder()
        elif pizza == "Seafood":
            self.__builder = SeafoodBuilder()

    def cook_default_pizza(self, size) -> None:
        self.builder.set_size(size)

    def cook_custom_pizza(self, size, sauce, dough, ingredients) -> None:
        self.builder.set_size(size)
        self.builder.set_sauce(sauce)
        self.builder.set_dough(dough)
        self.builder.set_ingredients(ingredients)
