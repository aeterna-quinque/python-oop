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
