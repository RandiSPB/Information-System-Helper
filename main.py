import math
from typing import Iterable


def entropia(ansamble: Iterable) -> float:
    return round(sum(tuple(map(lambda x: x[1] * message_info(x[1]), ansamble))), 5)


def message_info(x: float, base: int = 2) -> float:
    return round(-1 * math.log(x, base), 5)


def text_memory_coast(alphabet_power: int, num_pages: int, chars_per_page: int, measure_unit: str = 'bit',
                      order: str = '') -> str:
    units_map = {'bit': 1, 'byte': 8}
    order_map = {'': 1, 'kilo': 2 ** 10, 'mega': 2 ** 20, 'giga': 2 ** 30, 'tera': 2 ** 40}
    memory_cost = int(num_pages * chars_per_page * math.log(alphabet_power, 2))
    return f'Memory cost: {round(memory_cost  / units_map[measure_unit] / order_map[order], 5)} {order}{measure_unit}'

