from Pizzeria_5 import Pizza
import threading
import datetime


class CookingThread(threading.Thread):
    def __init__(self, name, pizza: Pizza):
        threading.Thread.__init__(self)
        self.name = name
        self.pizza = pizza

    def run(self):
        time = datetime.datetime.now()
        print(f"Start:\n"
              f"Thread {self.name}\t\tPizza {self.pizza.name} {self.pizza.size}\t\tTime {time}\n")
        Pizza.Pizza.cook(self.pizza)
        print(f"Finish:\n"
              f"Thread {self.name}\t\tPizza {self.pizza.name} {self.pizza.size}\t\tTime {datetime.datetime.now()}\n"
              f"Elapsed time: {datetime.datetime.now() - time}")
