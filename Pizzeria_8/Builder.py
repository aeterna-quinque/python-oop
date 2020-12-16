from abc import ABC, abstractmethod


class Builder(ABC):
    """

    Интерфейс Строителя.
    Объявляет создающие методы для различных шагов приготовления пиццы.

    """
    @property
    @abstractmethod
    def pizza(self):
        pass

    @property
    @abstractmethod
    def get_ingredients(self):
        pass

    @property
    @abstractmethod
    def get_sauces(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_size(self, value):
        pass

    @abstractmethod
    def set_dough(self, value):
        pass

    @abstractmethod
    def set_sauce(self, value):
        pass

    @abstractmethod
    def set_ingredients(self, value):
        pass

    @abstractmethod
    def get_certain_price(self, size):
        pass
