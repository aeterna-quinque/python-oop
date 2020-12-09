from Pizzeria_4.Menu.Barbecue import Barbecue
from Pizzeria_4.Menu.Seafood import Seafood
from Pizzeria_4.Menu.Pepperoni import Pepperoni
from Pizzeria_4.Order import Order
from Pizzeria_4.Pizza import Pizza
from functools import wraps


def event_info(func):
    """

    Декоратор event_info.
    Выводит в консоль имя функции и результат ее выполнения.
    Если произошла ошибка при выполнении функции, декоратор вызывает функцию заново.

    Parameters
    ----------
    func: function
        Функция, которую необходимо декорировать.

    Returns
    -------
    wrapper: function
        Декорированная функция.

    """

    @wraps(func)
    def wrapper(self):
        print(f"#Функция: {func.__name__}")
        handler = True
        while handler:
            try:
                func(self)
                handler = False
                print("#Функция успешно выполнена")
            except Exception:
                print(f"#Ошибка при выполнении функции")
                handler = True
        print("==========")

    return wrapper


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

    @event_info
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

    @event_info
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

    @event_info
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
        pizza = self.order.pizza_list[choice - 1]
        self.order.remove_pizza(choice)
        print(f"{pizza.name} - {pizza.size} - {pizza.price} had been successfully removed.\n")

    @event_info
    def cook_order(self):
        """

        Метод, имитирующий приготовление заказа.
        Из списка пицц заказа берет каждую пиццу и выполняет для нее метод cook, имитирующий ее приготовление.

        """
        for i in self.order.pizza_list:
            pizza = i
            pizza.cook()

    @event_info
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

    @event_info
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

    def create_pizza(self):
        """

        Метод для создания нового класса пиццы, наследуемого от абстрактного класса Pizza.

        """
        # Вводим название пиццы
        class_name = input("Name of pizza to add: ")

        # Вводим ингредиенты и их количество
        temp = []
        ing_n = int(input("Number of ingredients: "))
        for i in range(0, ing_n):
            ingredient = input(f"{i + 1}) ")
            temp.append(ingredient)
        ingredients_chosen = dict.fromkeys(temp, 1)

        # Вводим цены для размеров пиццы
        print("Input cost for every size of pizza")
        prices_chosen = {'small': 0, 'middle': 0, 'large': 0}
        for key, value in prices_chosen.items():
            value = int(input(f"{key} "))
            prices_chosen[key] = value

        # Конструктор новой пиццы
        def constructor(self, size, ingredients=None, name=class_name, prices=None, sauce='classic', dough='thin'):
            if prices is None:
                prices = prices_chosen
            if ingredients is None:
                ingredients = ingredients_chosen
            Pizza.__init__(self, size, ingredients, name, prices, sauce, dough)

        # Создание класса новой пиццы с использованием конструктора
        new_pizza = type(class_name, (Pizza,), {
            "__init__": constructor
        })

        # Добавление новой пиццы в меню
        self.menu.append(new_pizza("small"))
