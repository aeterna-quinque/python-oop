from Pizzeria_4.Pizza import Pizza


class Pepperoni(Pizza):
    """

    Класс Pepperoni, реализующий абстрактный класс Pizza.

    """
    def __init__(self, size, ingredients=None, name="Pepperoni", prices=None, sauce="classic", dough="thin"):
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
        Название пиццы. Если название не указано, то ставится имя Pepperoni.

        prices: dict{str: int}
        Цена для каждого размера пиццы. Если цены не указаны, конструктор ставит базовые цены для данной пиццы.

        sauce: str
        Название соуса для пиццы. Если соус не указан, конструктор устанавливает соус classic для данной пиццы.

        dough: str
        Вид теста, использующийся в пицце. Если тесто не указано, конструктор устанавливает тесто thin для данной пиццы.
        """
        if ingredients is None:
            ingredients = {'pepperoni': 2, 'mozzarella': 2, 'tomatoes': 2}
        if prices is None:
            prices = {'small': 400, 'middle': 500, 'large': 600}
        super().__init__(size, ingredients, name, prices, sauce, dough)
