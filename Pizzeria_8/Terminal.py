from tkinter import *
from tkinter.ttk import *
from .Director import Director
from .PizzaBuilders.BarbecueBuilder import BarbecueBuilder
from .PizzaBuilders.PepperoniBuilder import PepperoniBuilder
from .PizzaBuilders.SeafoodBuilder import SeafoodBuilder


class Terminal:

    def __init__(self):
        self.__menu = ['Barbecue', 'Pepperoni', 'Seafood']
        self.__order = {}
        self.__director = Director()
        self.main_window()

    def main_window(self):
        self.__root = Tk()
        self.__root.title('Order')
        self.__root.geometry('500x500')
        self.__root.resizable(0, 1)

        self.__order_frame = Frame(self.__root, relief=RAISED, borderwidth=1)
        for i in range(0, 3):
            self.__order_frame.columnconfigure(i, weight=1)
        self.__btn_frame = Frame(self.__root)

        __add_pizza_btn = Button(self.__btn_frame)
        __add_pizza_btn.config(text='Add pizza', command=self.pizza_window)

        __pay_order_btn = Button(self.__btn_frame)
        __pay_order_btn.config(text='Pay order', command=self.pay_order)

        __text_price_label = Label(self.__btn_frame, text='Current price:')
        self.__current_price_label = Label(self.__btn_frame, text=0, borderwidth=1, relief=SUNKEN, width=10)

        self.__order_frame.pack(fill=BOTH, expand=TRUE)
        self.__btn_frame.pack()
        self.__current_price_label.pack(side=TOP)
        __text_price_label.pack(side=TOP)
        __add_pizza_btn.pack(side=LEFT)
        __pay_order_btn.pack(side=LEFT)

        self.__root.mainloop()

    def pizza_window(self):
        try:
            self.__window.destroy()
        except AttributeError:
            pass
        finally:
            self.__window = Toplevel(self.__root)
        self.__window.title('Choose pizza')
        self.__window.resizable(0, 0)

        self.__pizza_frame = Frame(self.__window)
        self.__pizza_frame.grid(row=0)

        menu_label = Label(self.__pizza_frame, text='Pizza:')
        menu_label.grid(row=0, column=0, padx=5, pady=10)

        self.__menu_combo = Combobox(self.__pizza_frame, state='readonly')
        self.__menu_combo['values'] = self.__menu.copy()
        self.__menu_combo.grid(row=0, column=1, padx=5, pady=10)
        self.__menu_combo.current(0)
        self.__menu_combo.bind('<<ComboboxSelected>>', self.dynamic_price_counter)

        size_label = Label(self.__pizza_frame, text='Size:')
        size_label.grid(row=1, column=0, padx=5, pady=10)

        self.__size_combo = Combobox(self.__pizza_frame, state='readonly')
        self.__size_combo['values'] = ['small', 'middle', 'large']
        self.__size_combo.grid(row=1, column=1, padx=5, pady=10)
        self.__size_combo.current(0)
        self.__size_combo.bind('<<ComboboxSelected>>', self.dynamic_price_counter)

        Label(self.__pizza_frame, text='Price:').grid(row=2, column=0, padx=5, pady=10)
        self.__dynamic_price_label = Label(self.__pizza_frame, text='0', relief=SUNKEN, width=20)
        self.__dynamic_price_label.grid(row=2, column=1, padx=5, pady=10)
        self.__dynamic_price_label.bind('<Configure>', self.dynamic_price_counter)

        self.__default_button = Button(self.__pizza_frame, text='Add', command=self.add_default_pizza, state='normal')
        self.__default_button.grid(row=3, column=0, padx=5, pady=10)

        self.__customize_button = Button(self.__pizza_frame, text='Customize', command=self.custom_pizza_window, state='normal')
        self.__customize_button.grid(row=3, column=1, padx=5, pady=10)

    def dynamic_price_counter(self, event: Event):
        size = self.__size_combo.get()
        pizza = self.__menu_combo.get()
        self.__director.builder = pizza
        price = self.__director.builder.get_certain_price(size)
        self.__dynamic_price_label.config(text=f'{price}')

    def custom_pizza_window(self):
        self.__menu_combo.config(state='disabled')
        self.__size_combo.config(state='disabled')
        self.__default_button.config(state='disabled')
        self.__customize_button.config(state='disabled')

        self.__custom_frame = Frame(self.__window)
        self.__custom_frame.grid(row=1)

        pizza = self.__menu_combo.get()
        self.__director.builder = pizza

        sauce_label = Label(self.__custom_frame, text='Sauce:')
        sauce_label.grid(row=0, column=0, padx=5, pady=10)
        self.__sauce_combo = Combobox(self.__custom_frame, state='readonly')
        self.__sauce_combo['values'] = self.__director.builder.get_sauces
        self.__sauce_combo.grid(row=0, column=1, padx=5, pady=10)
        self.__sauce_combo.current(0)

        dough_label = Label(self.__custom_frame, text='Dough:')
        dough_label.grid(row=1, column=0, padx=5, pady=10)
        self.__dough_combo = Combobox(self.__custom_frame, state='readonly')
        self.__dough_combo['values'] = ['thin', 'thick', 'crispy']
        self.__dough_combo.grid(row=1, column=1, padx=5, pady=10)
        self.__dough_combo.current(0)

        ingredients = self.__director.builder.get_ingredients
        self.__spins = []
        i = 2

        for key in ingredients.keys():
            Label(self.__custom_frame, text=f'{key}').grid(row=i, column=0)
            self.__spins.append(Spinbox(self.__custom_frame, from_=0, to=3, width=5))
            self.__spins[i-2].grid(row=i, column=1)
            i += 1

        add_customize_button = Button(self.__custom_frame, text='Add', command=self.add_custom_pizza)
        add_customize_button.grid(row=i, columnspan=2)

    def add_default_pizza(self):
        size = self.__size_combo.get()
        self.__director.cook_default_pizza(size)
        pizza = self.__director.builder.pizza
        i = len(self.__order)
        self.__order[len(self.__order)] = pizza
        self.display_pizza()
        self.__window.destroy()

    def add_custom_pizza(self):
        size = self.__size_combo.get()
        sauce = self.__sauce_combo.get()
        dough = self.__dough_combo.get()
        ingredients = self.__director.builder.get_ingredients
        i = 0
        for key in ingredients.keys():
            ingredients[key] = self.__spins[i].get()
            i += 1

        self.__director.cook_custom_pizza(size, sauce, dough, ingredients)
        pizza = self.__director.builder.pizza
        self.__order[len(self.__order)] = pizza
        self.display_pizza()
        self.__window.destroy()

    def display_pizza(self):
        def show_pizza_info_wrap():
            self.show_pizza_info(rows)

        def remove_pizza_wrap():
            self.remove_pizza(rows)

        rows = len(self.__order)-1
        pizza = self.__order[rows]
        Label(self.__order_frame, text=f'{pizza.name}').grid(row=rows, column=0, sticky='W')
        Label(self.__order_frame, text=f'{pizza.size}').grid(row=rows, column=1, sticky='W')
        Label(self.__order_frame, text=f'{pizza.price}').grid(row=rows, column=2, sticky='W')
        Button(self.__order_frame, text='Info', command=show_pizza_info_wrap).grid(row=rows, column=3)
        Button(self.__order_frame, text='Remove', command=remove_pizza_wrap).grid(row=rows, column=4)

        self.count_price()

    def show_pizza_info(self, row):
        try:
            self.__info_window.destroy()
        except AttributeError:
            pass
        finally:
            self.__info_window = Toplevel(self.__root)
        self.__info_window.title('Pizza info')
        self.__info_window.resizable(0, 0)
        self.__info_window.grid()

        pizza = self.__order[row]

        Label(self.__info_window, text=f'Name: {pizza.name}').grid(row=0)
        Label(self.__info_window, text=f'Size: {pizza.size}').grid(row=1)
        Label(self.__info_window, text=f'Dough: {pizza.dough}').grid(row=2)
        Label(self.__info_window, text=f'Sauce: {pizza.sauce}').grid(row=3)
        Label(self.__info_window, text=f'Ingredients:').grid(row=4)
        i = 0
        for key, value in pizza.ingredients.items():
            Label(self.__info_window, text=f'{key}: {value}').grid(row=i + 5)
            i += 1
        Button(self.__info_window, text='Close', command=self.__info_window.destroy).grid(row=i + 5)

    def remove_pizza(self, row):
        for label in self.__order_frame.grid_slaves():
            if int(label.grid_info()["row"]) == row:
                label.grid_remove()
        self.__order.pop(row)

        self.count_price()

    def count_price(self):
        sum_price = 0
        for key, value in self.__order.items():
            sum_price += value.price
        self.__current_price_label.config(text=sum_price)

    def pay_order(self):
        for label in self.__order_frame.grid_slaves():
            label.grid_remove()
        self.__order.clear()
        self.__current_price_label.config(text=0)
