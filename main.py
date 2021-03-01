import math
from typing import Iterable, Tuple


def entropia(ansamble: Tuple[Tuple]) -> float:
    """
    Возвращает энтропию множества, в идеале в качестве аргумента подавать кортеж кортежей
    :param ansamble: Дискретный ансамбль в виде кортежа кортежей
    :return: Значение энтропии для данного ансамбля
    """
    return round(sum(tuple(map(lambda x: x[1] * message_info(x[1]), ansamble))), 5)


def message_info(x: float, base: int = 2) -> float:
    """
    Рассчитывает собственную информацию сообщения
    :param x: Вероятность данного сообщения
    :param base: Не обращать внимания и не менять
    :return: Возвращает собственное кол-во информации сообщения в битах
    """
    return round(-1 * math.log(x, base), 5)


def text_memory_coast(alphabet_power: int, num_pages: int, chars_per_page: int) -> str:
    """
    Расчет размера занимаемого места
    :param alphabet_power: Мощность алфавита
    :param num_pages: Кол-во страниц
    :param chars_per_page: Символов на странице
    :return: Форматированная строка с размером файла
    """
    return f'Memory cost: {num_pages * chars_per_page * math.log(alphabet_power, 2)}'


def min_bit(number: int) -> int:
    """
    Кол-во битов для хранения натуральных чисел меньше энного
    :param number: Последнее число которое должно хранится
    :return: Кол-во бит
    """
    exp = 1
    while 2 ** exp < number:
        exp += 1
    return exp


def unit_converter(value: float, start_measure_unit: str = 'bit', start_order: str = '', res_measure_unit: str = 'byte',
                   res_order: str = '') -> str:
    """
    Функция для перевода из одних единиц в другие
    :param value: Значение
    :param start_measure_unit: Единицы измерения входного числа
    :param start_order: Порядок единиц измерения входного числа
    :param res_measure_unit: Выходные единицы измерения
    :param res_order: Порядок выходной единицы измерения
    :return: Форматирования строка с начальным и конечным значение
    """
    units_map = {'bit': 1, 'byte': 8}
    order_map = {'': 1, 'kilo': 2 ** 10, 'mega': 2 ** 20, 'giga': 2 ** 30, 'tera': 2 ** 40}
    bit_value = value * units_map[start_measure_unit] * order_map[start_order]
    bit_value /= units_map[res_measure_unit] * order_map[res_order]
    return f'{value} {start_order}{start_measure_unit} = {bit_value} {res_order}{res_measure_unit}'


print(unit_converter(8, 'byte', 'kilo', 'bit'))