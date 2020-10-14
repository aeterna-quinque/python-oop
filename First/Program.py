import csv

from typing import List, Any

"""Задание 1. Базовые возможности Python

Данная программа реализует преобразования с введеным пользователем списком вещественных чисел.

Алгоритм:
1) Ввод списка вещественных чисел;
2) Умножение каждого числа в списке на 0.13;
3) Выбор пользователем типа сортировки списка (по возрастанию или по убыванию);
4) Сортировка списка;
5) Вывод чисел из списка, округленных до сотых;
6) Выбор пользователем варианта записи чисел в csv-файл (округлить числа в файле или нет);
7) Запись списка чисел в csv-файл.

Notes
-----
Типом файла для записи данных был выбран csv-тип.
Причины выбора данного типа:
1) Csv-тип удобен для дальнейшей обработки данных.
2) Запись в csv-файл проста в реализации.

Для документирования кода был выбран NumPy стиль документирования.
Причины выбора данного стиля:
1) Удобство в понимании.
2) Структуризация документации по блокам.
3) Мне не нравится стандартная документация в питоне.
Официальный гайд по документации NumPy: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard

"""


def float_check(n: Any) -> bool:
    """

    Данная функция проверяет является ли значение передаваемой переменной вещественным числом.

    Parameters
    ----------
    n: :obj:'float', optional
        Переменная, которую необходимо проверить.

    Returns
    -------
    bool
        True если в переменной хранится вещественное число, False в противном случае.

    """
    try:
        float(n)
        return True
    except ValueError:
        return False


def create_num_list() -> List[float]:
    """

    Данная функция создает список вещественных чисел на основе введенных пользователем данных.
    Число может быть введено как через точку, так и через запятую.
    Для завершения ввода чисел необходимо ввести строку, содержащую любой иной символ, помимо точки, запятой и цифр.

    Returns
    -------
    numbers: list of float
        Список введенных пользователем вещественных чисел.

    """
    numbers = []
    while True:
        n = input().replace(',', '.')
        if float_check(n):
            numbers.append(float(n))
        else:
            break
    return numbers


def multiply_num_list(numbers: List[float]) -> List[float]:
    """

    Данная функция умножает каждый элемент во входном списке вещественных чисел на 0.13.

    Parameters
    ----------
    numbers: list of float
        Входной список вещественных чисел.

    Returns
    -------
    numbers: list of float
        Список вещественных чисел из входного списка, умноженных на 0.13.

    """
    for i in range(len(numbers)):
        numbers[i] *= 0.13
    return numbers


def sort_num_list(numbers: List[float]) -> List[float]:
    """

    Данная функция сортирует входной список в зависимости от выбора пользователя.

    Parameters
    ----------
    numbers: list of float
        Входной список вещественных чисел.

    Returns
    -------
    numbers: list of float
        Список вещественных чисел, отстортированный по возрастанию или по убыванию.
        Если пользователь вводит значение, не соответствующее ни одному из возможных,
        то функция возвращает пустой список.

    """
    sort_type = input()
    if not sort_type.isdigit() or (int(sort_type) != 1 and int(sort_type) != 0):
        return []
    numbers = sorted(numbers, reverse=bool(int(sort_type)))
    return numbers


def output_num_list(numbers: List[float]):
    """

    Данная процедура выводит список вещественных чисел, округленных до сотых,
    в виде строки, где числа разделены пробелом.

    Parameters
    ----------
    numbers: list of float
        Входной список вещественных чисел.

    """
    result = ""
    for i in range(len(numbers)):
        result += f"{str(round(numbers[i], 2))} "
    print(result)


def write_in_file(numbers: List[float]) -> bool:
    """

    Данная функция записывает входной список вещественных чисел в файл numbers.csv.

    Notes
    -----
    Предыдущие значения в файле numbers.csv удаляются.

    Parameters
    ----------
    numbers: list of float
        Входной список вещественных чисел.

    Returns
    -------
    bool
        True если запись в файл прошла успешно, False в противном случае.

    """
    try:
        choice = bool(int(input()))
        if choice:
            for i in range(len(numbers)):
                numbers[i] = round(numbers[i], 2)
        with open("numbers.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(numbers)
        return True
    except ValueError:
        return False


# Здесь выполняется код программы.
# Для осуществления проверки ввода используется бесконечный цикл while True
def main():
    # Цикл ввода списка вещественных чисел
    print("Введите числа. Чтобы перестать вводить числа, введите что-то другое")
    while True:
        nums = create_num_list()
        if len(nums) > 0:
            break
        print("Введите хотя бы одно число")

    # Выполнение функции умножения
    multi_nums = multiply_num_list(nums)

    # Цикл сортировки списка
    print("Выберите тип сортировки\nПо возрастанию - 0\tПо убыванию - 1")
    while True:
        sorted_nums = sort_num_list(multi_nums)
        if len(sorted_nums) > 0:
            break
        print("Вы ввели неверное значение. Введите новое")

    # Вывод отсортированного списка
    output_num_list(sorted_nums)

    # Цикл записи в csv-файл
    print("Округлить числа в файле?\nНет - 0\tДа - 1")
    while True:
        choice = write_in_file(sorted_nums)
        if choice:
            break
        print("Вы ввели неверное значение. Введите новое")


# Вызов main()
if __name__ == "__main__":
    main()
