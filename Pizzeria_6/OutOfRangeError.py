class OutOfRangeError(Exception):

    def __init__(self, ingredient):
        self.ingredient = ingredient

    def set_default(self):
        print(f"Default number of portions set for {self.ingredient} - 2\n")
        return 2

