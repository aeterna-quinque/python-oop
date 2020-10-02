from Pizzeria.Pizza import Pizza


class Pepperoni(Pizza):

    def __init__(self, size, ingredients=None, name="Pepperoni", prices=None, sauce="classic", dough="thin"):
        if ingredients is None:
            ingredients = {'pepperoni': 2, 'mozzarella': 2, 'tomatoes': 2}
        if prices is None:
            prices = {'small': 400, 'middle': 500, 'large': 600}
        super().__init__(size, ingredients, name, prices, sauce, dough)
