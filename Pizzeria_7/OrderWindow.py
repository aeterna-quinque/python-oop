from tkinter import *
from tkinter.ttk import *
from Pizzeria_7.Terminal import Terminal


class OrderWindow:
    def __init__(self):
        self.terminal = Terminal(1)
        self.root = Tk()
        self.root.title('Order')
        self.root.geometry('500x500')
        self.root.resizable(0, 1)

        self.order_frame = Frame(self.root, relief=RAISED, borderwidth=1)
        for i in range(0, 3):
            self.order_frame.columnconfigure(i, weight=1)
        self.btn_frame = Frame(self.root)

        self.add_pizza_btn = Button(self.btn_frame)
        self.add_pizza_btn.config(text='Add pizza', command=self.add_pizza_window)

        self.pay_order_btn = Button(self.btn_frame)
        self.pay_order_btn.config(text='Pay order', command=self.pay_order)

        self.text_price_label = Label(self.btn_frame, text='Current price:')
        self.current_price_label = Label(self.btn_frame, text=0, borderwidth=1, relief=SUNKEN, width=10)

        self.order_frame.pack(fill=BOTH, expand=TRUE)
        self.btn_frame.pack()
        self.text_price_label.pack(side=TOP)
        self.current_price_label.pack(side=TOP)
        self.add_pizza_btn.pack(side=LEFT)
        self.pay_order_btn.pack(side=LEFT)

        self.root.mainloop()

    def add_pizza_window(self):
        def change_price_wrap(event):
            pizza_menu = self.terminal.menu.copy()
            pizza = pizza_menu.pop(self.menu_combo.current())
            size = self.size_combo.get()
            price = pizza.price_counter(size)
            price_label.config(text=f'{price}')

        self.window = Toplevel(self.root)
        self.window.title('Add pizza')
        self.window.resizable(0, 0)

        self.apf = Frame(self.window)
        self.apf.grid(row=0)

        menu_label = Label(self.apf, text='Pizza:')
        menu_label.grid(row=0, column=0, padx=5, pady=10)
        self.menu_combo = Combobox(self.apf, state='readonly')
        self.menu_combo['values'] = self.terminal.get_pizza_names()
        self.menu_combo.grid(row=0, column=1, padx=5, pady=10)
        self.menu_combo.current(0)
        self.menu_combo.bind('<<ComboboxSelected>>', change_price_wrap)

        size_label = Label(self.apf, text='Size:')
        size_label.grid(row=1, column=0, padx=5, pady=10)
        self.size_combo = Combobox(self.apf, state='readonly')
        self.size_combo['values'] = ['small', 'middle', 'large']
        self.size_combo.grid(row=1, column=1, padx=5, pady=10)
        self.size_combo.current(0)
        self.size_combo.bind('<<ComboboxSelected>>', change_price_wrap)

        dough_label = Label(self.apf, text='Dough:')
        dough_label.grid(row=2, column=0, padx=5, pady=10)
        self.dough_combo = Combobox(self.apf, state='readonly')
        self.dough_combo['values'] = ['thin', 'thick', 'crispy']
        self.dough_combo.grid(row=2, column=1, padx=5, pady=10)
        self.dough_combo.current(0)

        sauce_label = Label(self.apf, text='Sauce:')
        sauce_label.grid(row=3, column=0, padx=5, pady=10)
        self.sauce_combo = Combobox(self.apf, state='readonly')
        self.sauce_combo['values'] = ['classic', 'pesto', 'BBQ', 'bechamel']
        self.sauce_combo.grid(row=3, column=1, padx=5, pady=10)
        self.sauce_combo.current(0)

        price_text_label = Label(self.apf, text='Price:').grid(row=4, column=0, padx=5, pady=10)
        price_label = Label(self.apf, text='0', relief=SUNKEN, width=20)
        price_label.grid(row=4, column=1, padx=5, pady=10)

        confirm_btn = Button(self.apf, text='Confirm', command=self.ingredients_window)
        confirm_btn.grid(row=5, columnspan=2, padx=5, pady=10)

    def ingredients_window(self):
        try:
            self.inf.destroy()
        except AttributeError:
            pass
        finally:
            self.inf = Frame(self.window)

        self.inf = Frame(self.window)
        self.inf.grid(row=1)

        self.menu_combo.config(state='disabled')

        pizza_id = self.menu_combo.current()

        pizza_menu = self.terminal.menu.copy()
        pizza = pizza_menu.pop(pizza_id)

        ings = pizza.ingredients

        self.labels = []
        self.spins = []

        i = 0
        for key, value in ings.items():
            self.labels.append(Label(self.inf, text=f'{key}'))
            self.labels[i].grid(row=i, column=0)
            self.spins.append(Spinbox(self.inf, from_=0, to=3, width=5))
            self.spins[i].grid(row=i, column=1)
            i += 1

        finish_btn = Button(self.inf, text='Finish', command=self.add_pizza_to_order)
        finish_btn.grid(row=i, columnspan=2)

    def add_pizza_to_order(self):
        pizza_menu = self.terminal.menu.copy()
        pizza = pizza_menu.pop(self.menu_combo.current())
        size = self.size_combo.get()
        ingredients = {}
        for i in range(0, len(self.labels)):
            key = self.labels[i].cget('text')
            value = self.spins[i].get()
            if value == '':
                value = 2
            ingredients[key] = value
        sauce = self.sauce_combo.get()
        dough = self.dough_combo.get()
        new_pizza = pizza.__class__(size, ingredients, pizza.name, pizza.prices, sauce, dough)
        self.terminal.order.add_pizza(new_pizza)
        self.display_pizza(new_pizza)
        self.window.destroy()

    def display_pizza(self, pizza):
        def show_pizza_info_wrap():
            self.show_pizza_info(pizza)

        def remove_pizza_wrap():
            self.remove_pizza(rows)

        rows = self.terminal.order.i
        Label(self.order_frame, text=f'{pizza.name}').grid(row=rows, column=0, sticky='W')
        Label(self.order_frame, text=f'{pizza.size}').grid(row=rows, column=1, sticky='W')
        Label(self.order_frame, text=f'{pizza.price}').grid(row=rows, column=2, sticky='W')
        Button(self.order_frame, text='Info', command=show_pizza_info_wrap).grid(row=rows, column=3)
        Button(self.order_frame, text='Remove', command=remove_pizza_wrap).grid(row=rows, column=4)
        price = self.terminal.order.price
        self.current_price_label.config(text=price)

    def show_pizza_info(self, pizza):
        try:
            self.info_window.destroy()
        except AttributeError:
            pass
        finally:
            self.info_window = Toplevel(self.root)

        self.info_window.title('Pizza info')
        self.info_window.resizable(0, 0)
        self.info_window.grid()

        Label(self.info_window, text=f'Name: {pizza.name}').grid(row=0)
        Label(self.info_window, text=f'Size: {pizza.size}').grid(row=1)
        Label(self.info_window, text=f'Dough: {pizza.dough}').grid(row=2)
        Label(self.info_window, text=f'Sauce: {pizza.sauce}').grid(row=3)
        Label(self.info_window, text=f'Ingredients:').grid(row=4)
        ings = pizza.ingredients
        i = 0
        for key, value in ings.items():
            Label(self.info_window, text=f'{key}: {value}').grid(row=i + 5)
            i += 1
        Button(self.info_window, text='Close', command=self.info_window.destroy).grid(row=i + 5)

    def remove_pizza(self, rows):
        for label in self.order_frame.grid_slaves():
            if int(label.grid_info()["row"]) == rows:
                label.grid_remove()
        self.terminal.order.remove_pizza(rows)
        price = self.terminal.order.price
        self.current_price_label.config(text=price)

    def pay_order(self):
        for label in self.order_frame.grid_slaves():
            label.grid_remove()
        self.terminal.order.clear_order()
        self.current_price_label.config(text=0)
