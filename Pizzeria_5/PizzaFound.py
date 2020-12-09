class PizzaFound(Exception):
    """

    Класс исключений PizzaFound.
    Служит в качестве флага для нахождения пиццы.

    """
    def __init__(self, pizza_name):
        self.pizza_name = pizza_name

    def __str__(self):
        return f"Your choice - {self.pizza_name}\n"
