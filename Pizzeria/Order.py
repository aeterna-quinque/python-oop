<<<<<<< HEAD
from Pizzeria.Pizza import Pizza


class Order:
    """

    Класс Order.
    Имитирует заказ пользователя.

    Attributes
    ----------
    __price: int
        Суммарная стоимость заказа.

    __id: int
        Id заказа. Соответствует Id терминала, на котором принимается заказ.

    __pizza_list: list of pizza
        Список пицц, содержащихся в данном заказе.

    """
    __price = 0

    def __init__(self, order_id, pizza=None):
        """

        Констуктор класса.

        Parameters
        ----------
        order_id: int
            Id заказа.

        pizza: list of pizza
            Список пицц. Если пицца не передается в конструктор, то создается пустой список.

        """
        if pizza is None:
            pizza = []
        self.__id = order_id
        self.__pizza_list = pizza

    @property
    def price(self):
        """
        Геттер аттрибута price.
        """
        return self.__price

    @property
    def id(self):
        """
        Геттер аттрибута id.
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        Сеттер аттрибута id.
        """
        self.__id = value

    @property
    def pizza_list(self):
        """
        Геттер аттрибута pizza_list.
        """
        return self.__pizza_list

    @pizza_list.setter
    def pizza_list(self, value: Pizza):
        """
        Сеттер аттрибута pizza_list.
        """
        self.__pizza_list.append(value)
        self.__price += value.price

    def add_pizza(self, pizza: Pizza):
        """

        Метод для добавления пиццы в заказ.

        Parameters
        ----------
        pizza: Pizza
            Пицца, которую необходимо добавить в заказ.

        """
        self.__pizza_list.append(pizza)
        self.__price += pizza.price

    def remove_pizza(self, pizza_id):
        """

        Метод для удаления пиццы из заказа.

        Parameters
        ----------
        pizza_id: int
            Номер пиццы, которую необходимо убрать из заказа.

        """
        pizza = self.__pizza_list.pop(pizza_id-1)
        self.__price -= pizza.price

    def clear_order(self):
        """

        Метод, очищающий список заказа.

        """
        self.pizza_list.clear()
=======
from Pizzeria.Pizza import Pizza


class Order:
    __id = 0
    __pizza_list = []
    __price = 0

    def __init__(self, order_id, pizza=None):
        if pizza is None:
            pizza = []
        self.__id = order_id
        self.__pizza_list = pizza

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def pizza_list(self):
        return self.__pizza_list

    @pizza_list.setter
    def pizza_list(self, value: Pizza):
        self.__pizza_list.append(value)
        self.__price += value.price

    def add_pizza(self, pizza: Pizza):
        self.__pizza_list.append(pizza)
        self.__price += pizza.price

    def remove_pizza(self, pizza_id):
        pizza = self.__pizza_list.pop(pizza_id)
        self.__price -= pizza.price

    def clear_order(self):
        self.pizza_list.clear()
>>>>>>> 363667d4eb33893966e0d4dc13bd255876e8125e
