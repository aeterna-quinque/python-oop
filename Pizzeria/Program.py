<<<<<<< HEAD
from Pizzeria.Terminal import Terminal


# Функция main, в которой выполняется программа
def main():
    # Создаем терминал при помощи конструктора
    t1 = Terminal(1)
    # Выводим меню
    t1.display_menu()
    # Выбираем пиццу и добавляем ее в заказ
    t1.choose_pizza()
    t1.choose_pizza()
    t1.choose_pizza()
    # Убираем пиццу из заказа
    t1.remove_pizza()
    # Выводим заказ
    t1.display_order()
    # Готовим заказ
    t1.cook_order()
    # Оплата заказа
    t1.pay_order()
    # Отображение заказа (заказ должен обнулиться и не содержать пиццу)
    t1.display_order()


# Вызов main
if __name__ == "__main__":
    main()
=======
from Pizzeria.Terminal import Terminal


def main():
    t1 = Terminal(1)
    t1.display_menu()
    t1.choose_pizza()
    t1.choose_pizza()
    t1.choose_pizza()
    t1.display_order()
    t1.pay_order()
    t1.display_order()


if __name__ == "__main__":
    main()
>>>>>>> 363667d4eb33893966e0d4dc13bd255876e8125e
