import math
from typing import Iterable, Tuple, Union


def input_args(cmd_messages: Tuple[str, ...] = ('Enter first param:', )) -> Tuple:
    """
    Функция для ввода аргументов в рантайме
    :param cmd_messages: Кортеж с текстовыми литералами для ввода аргументов -> кол-во аргументов = кол-во литералов
    :return: кортеж с аргументами
    """
    params = []
    for cmd_message in cmd_messages:
        param = input(cmd_message + '\n')
        params.append(param)
    return tuple(params)


def entropia(ansamble: Tuple[Tuple[str, float], ...]) -> float:
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


def min_bit(number: int, base: int = 2) -> int:
    """
    Кол-во битов для хранения натуральных чисел меньше энного
    :param number: Последнее число которое должно хранится
    :param base: Количество состояний, нужно например в задачу про лампочку в обычном виде (бит -> 0,1)
    :return: Кол-во бит
    """
    exp = 1
    while base ** exp < number:
        exp += 1
    return exp


def unit_converter(value: Union[float, int], start_measure_unit: str = 'bit', start_order: str = '',
                   res_measure_unit: str = 'byte', res_order: str = '', format_out: bool = True) -> Union[str, int]:
    """
    Функция для перевода из одних единиц в другие
    :param value: Значение
    :param start_measure_unit: Единицы измерения входного числа
    :param start_order: Порядок единиц измерения входного числа
    :param res_measure_unit: Выходные единицы измерения
    :param res_order: Порядок выходной единицы измерения
    :param format_out: Вывести форматированный вывод
    :return: Либо строка либо кол-во бит
    """
    units_map = {'bit': 1, 'byte': 8}
    order_map = {'': 1, 'kilo': 2 ** 10, 'mega': 2 ** 20, 'giga': 2 ** 30, 'tera': 2 ** 40}
    try:
        bit_value = value * units_map[start_measure_unit] * order_map[start_order]
        bit_value /= units_map[res_measure_unit] * order_map[res_order]
        if format_out:
            return f'{value} {start_order}{start_measure_unit} = {bit_value} {res_order}{res_measure_unit}'
        else:
            return int(bit_value)
    except KeyError as wrong_key:
        return f'Неверно введена размерность - {wrong_key}'


def get_power(file_size: Union[float, int], chars_num: int, in_bits: bool = True) -> int:
    if in_bits:
        return 2 ** int(file_size / chars_num)
    else:
        args = input_args(('Введите единицы измерения (bit/byte):', 'Введите порядок ("", kilo, mega, giga):'))
        return get_power(unit_converter(file_size, *args, 'bit', format_out=False), chars_num)


print(get_power(11, 11264, False))
