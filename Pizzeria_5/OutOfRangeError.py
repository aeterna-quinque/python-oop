class OutOfRangeError(Exception):
    """

    Класс исключений OutOfRangeError.
    Вызывается при выходе значения за допустимые рамки в методе ingredients_interface.

    """
    def __init__(self, ingredient):
        self.ingredient = ingredient

    def set_default(self):
        """

        Метод, который возвращает фиксированное значение в случае вызова данного исключения.

        """
        print(f"Default number of portions set for {self.ingredient} - 2\n")
        return 2

