from abc import ABC, abstractmethod
from Pizzeria_5.OutOfRangeError import OutOfRangeError
from functools import wraps
from time import sleep
from random import randint


def ingredients_decorator(ingredients_interface):
    """

    Декоратор ingredients_decorator.
    Служит интерфейсом для ввода количества ингредиентов пиццы.

    Parameters
    ----------
    ingredients_interface: function
        Функция ввода ингредиента. ингредиента.

    Returns
    -------
    wrapper: function
        Декорированная функция.

    """
    @wraps(ingredients_interface)
    def wrapper(self, first_call, ingredient):
        if first_call:
            print("\nEnter number of portions for every ingredient.\n"
                  "1 portion = 50 grams.\n"
                  "You can choose 0 to 3 portions for each.")
        print(f"{ingredient} - ", end="")
        return ingredients_interface(self, first_call, ingredient)

    return wrapper


class Pizza(ABC):
    """

    Абстрактный класс Pizza
    Данный класс является родительским классом для всех классов типов пицц, хранящихся в папке Menu.

    Attributes
    ----------
    __size: str
        Размер пиццы.

    __ingredients: dict{str: int}
        Ингридиенты и количество порций каждого ингридиента.

    __name: str
        Название пиццы.

    __prices: dict{str: int}
        Цена для каждого размера пиццы.

    __sauce: str
        Название соуса для пиццы.

    __dough: str
        Вид теста, использующийся в пицце.

    __price: int
        Цена для данной пиццы выбранного размера.

    Notes
    -----
    В данном классе абстрактный только конструктор.
    Использование абстрактного класса обусловлено логикой программы: допустимо создание лишь определенной пиццы.

    В данном классе есть один приватный метод __price_counter.
    Его приватность обусловлена тем, что он используется только в этом классе, а также он устанавливает цену на данную
    пиццу, а следовательно из соображений безопасности лучше запретить его вызов в main.

    """

    @abstractmethod
    def __init__(self, size, ingredients, name, prices=None, sauce="classic", dough="thin"):
        """

        Констуктор класса.

        Parameters
        ----------
        size: str
        Размер пиццы.

        ingredients: dict{str: int}
        Ингридиенты и количество порций каждого ингридиента.

        name: str
        Название пиццы.

        prices: dict{str: int}
        Цена для каждого размера пиццы. Если цены не указаны, констуктор ставит базовые цены для данной пиццы.

        sauce: str
        Название соуса для пиццы. Если соус не указан, конструктор устанавливает соус classic для данной пиццы.

        dough: str
        Вид теста, использующийся в пицце. Если тесто не указано, конструктор устанавливает тесто thin для данной пиццы.

        """
        self.__size = size
        self.__ingredients = ingredients
        self.__name = name
        if prices is None:
            prices = {'small': 400, 'middle': 500, 'large': 600}
        self.__prices = prices
        self.__sauce = sauce
        self.__dough = dough
        self.__price = self.__price_counter(size)

    @property
    def name(self):
        """
        Геттер аттрибута name.
        """
        return self.__name

    @property
    def price(self):
        """
        Геттер аттрибута price.
        """
        return self.__price

    @property
    def prices(self):
        """
        Геттер аттрибута prices.
        """
        return self.__prices

    @property
    def size(self):
        """
        Геттер аттрибута size.
        """
        return self.__size

    @property
    def sauce(self):
        """
        Геттер аттрибута sauce.
        """
        return self.__sauce

    @sauce.setter
    def sauce(self, value):
        """
        Сеттер аттрибута sauce.
        """
        self.__sauce = value

    @property
    def dough(self):
        """
        Геттер аттрибута dough.
        """
        return self.__dough

    @dough.setter
    def dough(self, value):
        """
        Сеттер аттрибута dough.
        """
        self.__dough = value

    @property
    def ingredients(self):
        """
        Геттер аттрибута ingredients.
        """
        return self.__ingredients

    def __price_counter(self, size):
        """

        Приватный метод для расчета цены конкретной пиццы.
        Проверяет есть ли указанный размер в словаре размеров prices. Если есть, то возвращает цену для соответствующего
        размера. В противном случае вернет 0.

        Parameters
        ----------
        size: str
            Размер пиццы.

        Returns
        -------
        ans: int
            Цена пиццы конкретного размера.

        """
        prices = self.prices
        ans = 0
        if size in prices:
            ans = prices[size]
        return ans

    def cook(self):
        """

        Метод, имитирующий приготовление конкретной пиццы.
        Пишет основные шаги приготовления пиццы:
        1) Готовка указанного для данной пиццы теста;
        2) Готовка указанного для данной пиццы соуса;
        3) Добавление ингредиентов для данной пиццы;
        4) Запекание пиццы;
        5) Нарезка пиццы;
        6) Упаковка пиццы.

        """
        print(f"{self.name} {self.size}: Cooking {self.dough} dough.\n")
        sleep(randint(1, 3))
        print(f"{self.name} {self.size}: Cooking {self.sauce} sauce.\n")
        sleep(randint(1, 3))
        print(f"{self.name} {self.size}: Putting {self.sauce} on dough.\n")
        sleep(randint(0, 1))
        text = f"{self.name} {self.size}: Adding ingredients:\n"
        keys_list = list(self.__ingredients.keys())
        for i in range(0, len(keys_list)):
            text += f"{keys_list[i]} - {self.__ingredients[keys_list[i]]} portion(s)\n"
        print(text)
        sleep(randint(1, 3))
        print(f"Cooking {self.name} {self.size} pizza...\n")
        sleep(randint(3, 6))
        print(f"Slicing {self.name} {self.size} pizza...\n")
        sleep(randint(0, 1))
        print(f"Packing {self.name} {self.size} pizza...\n")
        sleep(randint(0, 1))
        print(f"Your {self.name} {self.size} pizza is ready!\n")

    def change_dough(self):
        """

        Метод, позволяющий установить/изменить тесто для данной пиццы.
        Запрашивает ввод типа теста для данной пиццы у пользователя. Если введенный тип есть в списке допустимых типов
        теста, то устанавливает для данной пиццы введенный тип теста.
        В противном случае устанавливает тонкое(thin) тесто.

        """
        print("\nSelect dough for pizza:")
        doughs = ['thin', 'thick', 'crispy']
        text = ""
        for i in doughs:
            text += f"{i}\t"
        print(text)
        choice = input()
        if choice not in doughs:
            print(f"There is no option for {choice} dough. Thin dough set.\n")
            choice = doughs[0]
        self.dough = choice

    def change_sauce(self):
        """

        Метод, позволяющий установить/изменить соус для данной пиццы.
        Запрашивает ввод соуса для данной пиццы у пользователя. Если введенный соус есть в списке допустимых соусов,
        то устанавливает для данной пиццы введенный соус.
        В противном случае устанавливает классический(classic) соус.

        """
        print("\nSelect sauce for pizza:")
        sauces = ['classic', 'pesto', 'BBQ', 'bechamel']
        text = ""
        for i in sauces:
            text += f"{i}\t"
        print(text)
        choice = input()
        if choice not in sauces:
            print(f"There is no option for {choice} sauce. Classic sauce set.\n")
            choice = sauces[0]
        self.sauce = choice

    def change_ingredients(self):
        """

        Метод, позволяющий установить/изменить количество того или иного ингредиента для пиццы.
        Берет словарь ингредиентов данной пиццы и для каждого игредиента вызывает метод ingredients_interface
        и присваивает каждому ингредиенту количество порций, которое возвратил метод ingredients_interface.

        """
        first_call = True
        keys_list = list(self.__ingredients.keys())
        for i in range(0, len(keys_list)):
            self.__ingredients[keys_list[i]] = self.ingredients_interface(first_call, keys_list[i])
            first_call = False

    @ingredients_decorator
    def ingredients_interface(self, first_call, ingredient):
        """

        Метод, запрашивающий у пользователя количество порций для конкретного ингридиента.
        Если метод вызывается впервые для данной пиццы, то выводится справка по ингредиентам.
        Если выбранное количество порций не является допустимым, то возвращает базовое значение, равное 2.

        Parameters
        ----------
        first_call: bool
            Указывает, является ли вызов данного метода первым для конкретной пиццы.
        ingredient: str
            Имя ингредиента.

        Returns
        -------
            portion: int
                Количество порций конкретного ингредиента.
        """
        try:
            portion = int(input())
            if portion not in range(0, 4):
                raise OutOfRangeError(ingredient)

        except OutOfRangeError as e:
            return e.set_default()

        except ValueError as e:
            print(f"{e.__str__()}\nNumber of portions set to 2.\n")
            return 2

        else:
            return portion
