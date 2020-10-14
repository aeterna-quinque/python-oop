from Pizzeria.Menu.Barbecue import Barbecue
from Pizzeria.Menu.Seafood import Seafood
from Pizzeria.Menu.Pepperoni import Pepperoni
from Pizzeria.Order import Order


class Terminal:
    """

    Класс Terminal.
    Имитирует работу терминала для заказа пиццы.

    Attributes
    ----------
    __id: int
        Id терминала.

    __menu: list of pizza
        Список-меню доступных для заказа пицц.

    __order: Order
        Заказ на данном терминале.

    """
    def __init__(self, t_id, menu=None):
        """

        Конструктор класса.

        Parameters
        ----------
        t_id: int
            Id терминала.

        menu: list of pizza
            Список-меню доступных для заказа пицц. Если не передается в конструктор, то создается базовый список.

        """
        if menu is None:
            menu = [Barbecue('small'), Seafood('small'), Pepperoni('small')]
        self.__id = t_id
        self.__menu = menu
        self.__order = Order(t_id)

    @property
    def menu(self):
        """
        Геттер аттрибута menu.
        """
        return self.__menu

    @property
    def order(self):
        """
        Геттер аттрибута order.
        """
        return self.__order

    @order.setter
    def order(self, value: Order):
        """
        Сеттер аттрибута order.
        """
        self.__order = value

    def display_menu(self):
        """

        Метод, выводящий меню данного терминала.

        """
        text = "Menu:\n"
        i = 1
        for pizza in self.menu:
            text += f"{i}) {pizza.name}\n"
            for key, value in pizza.prices.items():
                text += f"\t{key} - {value}\n"
            i += 1
        print(text)

    def choose_pizza(self):
        """

        Метод для добавления пиццы в заказ.
        Запрашивает у пользователя ввод id пиццы из меню.
        Создает объект данной пиццы.
        Запрашивает ввод теста, соуса и ингредиентов для данной пиццы у пользователя.
        Добавляет данную пиццу в заказ.

        """
        pizza_id = int(input("Print id of pizza in menu to choose it: ")) - 1
        pizza_menu = self.menu.copy()
        pizza = pizza_menu.pop(pizza_id)
        s = input(f"Print size of {str.lower(pizza.name)} pizza:\nsmall\tmiddle\tlarge\n")
        pizza.change_dough()
        pizza.change_sauce()
        pizza.change_ingredients()
        new_pizza = pizza.__class__(s, pizza.ingredients, pizza.name, pizza.prices, pizza.sauce, pizza.dough)
        print(f"Added to your order:\n{new_pizza.name} - {new_pizza.size} - {new_pizza.price}\n")
        self.order.add_pizza(new_pizza)

    def remove_pizza(self):
        """

        Метод для удаления пиццы из заказа.
        Выводит все пиццы из заказа и запрашивает ввод id пиццы для удаления у пользователя.
        Удаляет выбранную пиццу из заказа.

        """
        print("Choose pizza to remove:")
        j = 1
        self.display_order()
        choice = int(input())
        pizza = self.order.pizza_list[choice-1]
        self.order.remove_pizza(choice)
        print(f"{pizza.name} - {pizza.size} - {pizza.price} had been successfully removed.\n")

    def cook_order(self):
        """

        Метод, имитирующий приготовление заказа.
        Из списка пицц заказа берет каждую пиццу и выполняет для нее метод cook, имитирующий ее приготовление.

        """
        for i in self.order.pizza_list:
            pizza = i
            pizza.cook()

    def pay_order(self):
        """

        Метод, имитирующий оплату заказа.
        Выводит стоимость заказа и запрашивает выбор пользователя: платить или нет.
        В зависимости от выбора пишет ответ.
        Очищает заказ.

        """
        choice = bool(int(input(f"Cost of your order: {self.order.price}.\nTo pay - 1\t Not to pay - 0\n")))
        if choice:
            print("Thank you for visiting our Pizzeria! Hope to see you again.")
        else:
            print("...You have become an ingredient for another pizza...")
        self.order.clear_order()

    def display_order(self):
        """

        Метод для вывода заказа.

        """
        text = "Order:\n"
        j = 1
        for pizza in self.order.pizza_list:
            text += f"{j}) {pizza.name} - {pizza.size} - {pizza.price}\n"
            j += 1
        print(text)
