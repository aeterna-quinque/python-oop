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
