from Pizzeria_5 import Pizza
import threading
import datetime


class CookingThread(threading.Thread):
    """

    Класс CookingThread.
    Класс потока для приготовления пиццы.

    Attributes
    ----------
    name: str
        Имя потока.

    pizza: Pizza
        Пицца, которую готовит данный поток.

    """
    def __init__(self, name, pizza: Pizza):
        """

        Конструктор класса.

        Parameters
        ----------
        name: str
            Имя потока.

        pizza: Pizza.py
            Пицца, которую готовит данный поток.

        """
        threading.Thread.__init__(self)
        self.name = name
        self.pizza = pizza

    def run(self):
        """

        Метод, который фиксирует время начала приготовления, запускает процесс приготовления пиццы и фиксирует время
        окончания приготовления.

        """
        time = datetime.datetime.now()
        print(f"Start:\n"
              f"Thread {self.name}\t\tPizza {self.pizza.name} {self.pizza.size}\t\tTime {time}\n")
        Pizza.Pizza.cook(self.pizza)
        print(f"Finish:\n"
              f"Thread {self.name}\t\tPizza {self.pizza.name} {self.pizza.size}\t\tTime {datetime.datetime.now()}\n"
              f"Elapsed time: {datetime.datetime.now() - time}")
