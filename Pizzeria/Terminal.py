from Pizzeria.Menu.Barbecue import Barbecue
from Pizzeria.Menu.Seafood import Seafood
from Pizzeria.Menu.Pepperoni import Pepperoni
from Pizzeria.Order import Order


class Terminal:

    def __init__(self, t_id, menu=None):
        if menu is None:
            menu = [Barbecue('small'), Seafood('small'), Pepperoni('small')]
        self.__id = t_id
        self.__menu = menu
        self.__order = Order(t_id)

    @property
    def menu(self):
        return self.__menu

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value: Order):
        self.__order = value

    def display_menu(self):
        text = "Menu:\n"
        i = 1
        for pizza in self.menu:
            text += f"{i}) {pizza.name}\n"
            for key, value in pizza.prices.items():
                text += f"\t{key} - {value}\n"
            i += 1
        print(text)

    def choose_pizza(self):
        pizza_id = int(input("Print id of pizza in menu to choose it: ")) - 1
        pizza_menu = self.menu.copy()
        pizza = pizza_menu.pop(pizza_id)
        s = input(f"Print size of {str.lower(pizza.name)} pizza:\nsmall\tmiddle\tlarge\n")
        new_pizza = pizza.__class__(s, pizza.ingredients, pizza.name, pizza.prices, pizza.sauce, pizza.dough)
        print(f"Added to your order:\n{new_pizza.name} - {new_pizza.size} - {new_pizza.price}\n")
        self.order.pizza_list = new_pizza

    def pay_order(self):
        choice = bool(int(input(f"Cost of your order: {self.order.price}.\nTo pay - 1\t Not to pay - 0\n")))
        if choice:
            print("Thank you for visiting our Pizzeria! Hope to see you again.")
        else:
            print("...You have become an ingredient for another pizza...")
        self.order.clear_order()

    def display_order(self):
        text = "Order:\n"
        for pizza in self.order.pizza_list:
            text += f"{pizza.name} - {pizza.size} - {pizza.price}\n"
        print(text)
