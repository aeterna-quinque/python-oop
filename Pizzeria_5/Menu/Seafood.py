from Pizzeria_5.Pizza import Pizza


class Seafood(Pizza):
    """

    Класс Seafood, реализующий абстрактный класс Pizza.

    """
    def __init__(self, size, ingredients=None, name="Seafood", prices=None, sauce="bechamel", dough="thin"):
        """

        Конструктор класса.

        Parameters
        ----------
        size: str
            Размер пиццы.

        ingredients: dict{str: int}
        Ингридиенты и количество порций каждого ингридиента. Если ингредиенты не указаны, конструктор ставить базовые
        ингредиенты для данной пиццы.

        name: str
        Название пиццы. Если название не указано, то ставится имя Seafood.

        prices: dict{str: int}
        Цена для каждого размера пиццы. Если цены не указаны, конструктор ставит базовые цены для данной пиццы.

        sauce: str
        Название соуса для пиццы. Если соус не указан, конструктор устанавливает соус bechamel для данной пиццы.

        dough: str
        Вид теста, использующийся в пицце. Если тесто не указано, конструктор устанавливает тесто thin для данной пиццы.
        """
        if ingredients is None:
            ingredients = {'prawns': 2, 'mozzarella': 2, 'squid': 1, 'tuna': 1, 'tomatoes': 1}
        if prices is None:
            prices = {'small': 450, 'middle': 600, 'large': 750}
        super().__init__(size, ingredients, name, prices, sauce, dough)
