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


def text_memory_coast(alphabet_power: int, num_pages: int, chars_per_page: int, measure_unit: str = 'bit',
                      order: str = '') -> str:
    """
    Расчет размера занимаемого места
    :param alphabet_power: Мощность алфавита
    :param num_pages: Кол-во страниц
    :param chars_per_page: Символов на странице
    :param measure_unit: Единицы измерения
    :param order: Порядок единиц измерения
    :return: Форматированная строка с размером файла и единицой измерения
    """
    units_map = {'bit': 1, 'byte': 8}
    order_map = {'': 1, 'kilo': 2 ** 10, 'mega': 2 ** 20, 'giga': 2 ** 30, 'tera': 2 ** 40}
    memory_cost = int(num_pages * chars_per_page * math.log(alphabet_power, 2))
    try:
        return f'Memory cost: {round(memory_cost  / units_map[measure_unit] / order_map[order], 5)}' \
               f' {order}{measure_unit}'
    except KeyError as error:
        return f'Неправильно указана единициа измерений или порядок - {error}'


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


print(min_bit(255))
