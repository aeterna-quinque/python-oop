from abc import ABC, abstractmethod


class Pizza(ABC):
    __ingredients = {}
    __size = ""
    __sauce = ""
    __dough = ""
    __price = 0
    __prices = {}
    __name = ""

    @abstractmethod
    def __init__(self, size, ingredients, name, prices=None, sauce="classic", dough="thin"):
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
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        sizes = self.prices.keys()
        if value in sizes:
            self.__price = self.prices[value]

    @property
    def prices(self):
        return self.__prices

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        sizes = self.prices.keys()
        if value in sizes:
            self.__size = value
        else:
            raise ValueError("Wrong size.")

    @property
    def sauce(self):
        return self.__sauce

    @sauce.setter
    def sauce(self, value):
        sauces = ['classic', 'pesto', 'BBQ', 'bechamel']
        if value in sauces:
            self.__sauce = value
        else:
            raise ValueError("Wrong sauce.")

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        dough = ['thin', 'thick', 'crispy']
        if value in dough:
            self.__dough = value
        else:
            raise ValueError("Wrong dough.")

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        keys_list = list(self.__ingredients.keys())
        values_list = list(value)
        if keys_list > values_list:
            limit = len(values_list)
        else:
            limit = len(keys_list)
        for i in range(0, limit):
            if values_list[i] not in range(0, 4):
                values_list[i] = 2
            self.__ingredients[keys_list[i]] = values_list[i]
        for i in range(limit, len(self.__ingredients)):
            self.__ingredients[keys_list[i]] = 0

    def __price_counter(self, size):
        prices = self.prices
        ans = 0
        if size in prices:
            ans = prices[size]
        return ans

    def cook(self):
        text = f"Cooking {self.dough} dough.\n" \
               f"Cooking {self.sauce} sauce.\n" \
               f"Putting {self.sauce} on dough.\n" \
               "Adding ingredients:\n"
        for key, value in self.ingredients:
            text += f"{key} - {value} portion(s)\n"
        text += "Cooking pizza...\n" \
                "Slicing pizza...\n" \
                "Packing pizza...\n" \
                "Your pizza is ready!"
        print(text)

    def change_ingredients(self):
        first_call = True
        keys_list = list(self.__ingredients.keys())
        for i in range(0, len(keys_list)):
            self.__ingredients[keys_list[i]] = self.ingredients_interface(i, first_call)

    def ingredients_interface(self, i, first_call):
        if first_call:
            print("Enter number of portions for every ingredient.\n"
                  "1 portion = 50 grams.\n"
                  "You can choose 0 to 3 portions for each.\n")
        portion = int(input(f"{self.__ingredients[i]} - "))
        if portion in range(0, 4):
            return portion
        else:
            raise ValueError("Wrong number of portions.")
