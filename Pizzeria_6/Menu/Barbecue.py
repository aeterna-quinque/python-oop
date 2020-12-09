from Pizzeria_6.Pizza import Pizza


class Barbecue(Pizza):
    """

    Класс Barbecue, реализующий абстрактный класс Pizza.

    """
    def __init__(self, size, ingredients=None, name="Barbecue", prices=None, sauce="BBQ", dough="thin"):
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
        Название пиццы. Если название не указано, то ставится имя Barbecue.

        prices: dict{str: int}
        Цена для каждого размера пиццы. Если цены не указаны, конструктор ставит базовые цены для данной пиццы.

        sauce: str
        Название соуса для пиццы. Если соус не указан, конструктор устанавливает соус BBQ для данной пиццы.

        dough: str
        Вид теста, использующийся в пицце. Если тесто не указано, конструктор устанавливает тесто thin для данной пиццы.
        """
        if ingredients is None:
            ingredients = {'chicken ham': 2, 'champignons': 1, 'pineapple': 1, 'mozzarella': 2}
        if prices is None:
            prices = {'small': 350, 'middle': 450, 'large': 550}
        super().__init__(size, ingredients, name, prices, sauce, dough)
