from Pizzeria.Pizza import Pizza


class Seafood(Pizza):

    def __init__(self, size, ingredients=None, name="Seafood", prices=None, sauce="Bechamel", dough="thin"):
        if ingredients is None:
            ingredients = {'prawns': 2, 'mozzarella': 2, 'squid': 1, 'tuna': 1, 'tomatoes': 1}
        if prices is None:
            prices = {'small': 450, 'middle': 600, 'large': 750}
        super().__init__(size, ingredients, name, prices, sauce, dough)
