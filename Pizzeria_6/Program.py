import asyncio

from Pizzeria_6.Terminal import Terminal


# Функция main, в которой выполняется программа
async def main():
    # Создаем терминал при помощи конструктора
    t1 = Terminal(1)
    # Выводим меню
    await t1.display_menu()
    # Выбираем пиццу и добавляем ее в заказ
    await t1.choose_pizza()
    await t1.display_order()
    await t1.choose_pizza()
    # Убираем пиццу из заказа
    await t1.remove_pizza()
    # Выводим заказ
    await t1.display_order()
    # Готовим заказ
    await t1.cook_order()
    await asyncio.sleep(17)
    # Оплата заказа
    await t1.pay_order()
    # Отображение заказа (заказ должен обнулиться и не содержать пиццу)
    await t1.display_order()


# Вызов main
if __name__ == "__main__":
    asyncio.run(main())
