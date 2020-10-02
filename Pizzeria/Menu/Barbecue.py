from Pizzeria.Pizza import Pizza


class Barbecue(Pizza):

    def __init__(self, size, ingredients=None, name="Barbecue", prices=None, sauce="BBQ", dough="thin"):
        if ingredients is None:
            ingredients = {'chicken ham': 2, 'champignons': 1, 'pineapple': 1, 'mozzarella': 2}
        if prices is None:
            prices = {'small': 350, 'middle': 450, 'large': 550}
        super().__init__(size, ingredients, name, prices, sauce, dough)
