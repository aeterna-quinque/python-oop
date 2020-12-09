import datetime
from threading import Thread
import asyncio

from Pizzeria_6.Menu.Barbecue import Barbecue
from Pizzeria_6.Menu.Seafood import Seafood
from Pizzeria_6.Menu.Pepperoni import Pepperoni
from Pizzeria_6.Order import Order
from Pizzeria_6.Pizza import Pizza
from Pizzeria_6.PizzaFound import PizzaFound


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

    async def display_menu(self):
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

    async def choose_pizza(self):
        """

        Метод для добавления пиццы в заказ.
        Запрашивает у пользователя ввод id пиццы из меню.
        Создает объект данной пиццы.
        Запрашивает ввод теста, соуса и ингредиентов для данной пиццы у пользователя.
        Добавляет данную пиццу в заказ.

        """
        pizza_id = int(input("Print id of pizza in menu to choose it: ")) - 1
        try:
            if pizza_id in range(0, (len(self.menu))):
                raise PizzaFound(self.menu[pizza_id].name)

        except PizzaFound as e:
            print(e.__str__())
            pizza_menu = self.menu.copy()
            pizza = pizza_menu.pop(pizza_id)
            s = input(f"Print size of {str.lower(pizza.name)} pizza:\nsmall\tmiddle\tlarge\n")
            await pizza.change_dough()
            await pizza.change_sauce()
            await pizza.change_ingredients()
            new_pizza = pizza.__class__(s, pizza.ingredients, pizza.name, pizza.prices, pizza.sauce, pizza.dough)
            print(f"Added to your order:\n{new_pizza.name} - {new_pizza.size} - {new_pizza.price}\n")
            await self.order.add_pizza(new_pizza)

        else:
            print(f"Pizza with {pizza_id + 1} id not found!")

    async def remove_pizza(self):
        """

        Метод для удаления пиццы из заказа.
        Выводит все пиццы из заказа и запрашивает ввод id пиццы для удаления у пользователя.
        Удаляет выбранную пиццу из заказа.

        """

        try:
            print("Choose pizza to remove:")
            await self.display_order()
            choice = int(input())
            if (choice - 1) not in range(0, (len(self.order.pizza_list))):
                raise PizzaFound(choice)

        except PizzaFound as e:
            e.__str__()

        else:
            pizza = self.order.pizza_list[choice - 1]
            await self.order.remove_pizza(choice)
            print(f"{pizza.name} - {pizza.size} - {pizza.price} had been successfully removed.\n")

    async def cook_order(self):
        """

        Метод, имитирующий приготовление заказа.
        Из списка пицц заказа берет каждую пиццу и выполняет для нее метод cook, имитирующий ее приготовление.

        """
        async def __run(thread_name, pizza_object):
            time = datetime.datetime.now()
            print(f"Start:\n"
                  f"Thread {thread_name}\t\tPizza {pizza_object.name} {pizza_object.size}\t\tTime {time}\n")
            await pizza_object.cook()
            print(f"Finish:\n"
                  f"Thread {thread_name}\t\tPizza {pizza_object.name} {pizza_object.size}\t\t"
                  f"Time {datetime.datetime.now()}\n "
                  f"Elapsed time: {datetime.datetime.now() - time}")

        def __start_loop(loop):
            asyncio.set_event_loop(loop)
            loop.run_forever()

        new_loop = asyncio.new_event_loop()
        t = Thread(target=__start_loop, args=(new_loop,))
        t.start()
        for i in self.order.pizza_list:
            pizza = i
            name = f"Thread{self.order.pizza_list.index(i) + 1}"
            asyncio.run_coroutine_threadsafe(__run(name, pizza), new_loop)

    async def pay_order(self):
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
        await self.order.clear_order()

    async def display_order(self):
        """

        Метод для вывода заказа.

        """
        text = "Order:\n"
        j = 1
        for pizza in self.order.pizza_list:
            text += f"{j}) {pizza.name} - {pizza.size} - {pizza.price}\n"
            j += 1
        print(text)

    async def create_pizza(self):
        class_name = input("Name of pizza to add: ")

        temp = []
        ing_n = int(input("Number of ingredients: "))
        for i in range(0, ing_n):
            ingredient = input(f"{i + 1}) ")
            temp.append(ingredient)
        ingredients_chosen = dict.fromkeys(temp, 1)

        print("Input cost for every size of pizza")
        prices_chosen = {'small': 0, 'middle': 0, 'large': 0}
        for key, value in prices_chosen.items():
            value = int(input(f"{key} "))
            prices_chosen[key] = value

        def constructor(self, size, ingredients=None, name=class_name, prices=None, sauce='classic', dough='thin'):
            if prices is None:
                prices = prices_chosen
            if ingredients is None:
                ingredients = ingredients_chosen
            Pizza.__init__(self, size, ingredients, name, prices, sauce, dough)

        new_pizza = type(class_name, (Pizza,), {
            "__init__": constructor
        })

        self.menu.append(new_pizza("small"))
