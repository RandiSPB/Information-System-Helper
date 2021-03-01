import math
from typing import Iterable


def entropia(ansamble: Iterable) -> float:
    return round(sum(tuple(map(lambda x: x[1] * message_info(x[1]), ansamble))), 5)


def message_info(x: float, base: int = 2) -> float:
    return round(-1 * math.log(x, base), 5)


probability_distribution = (() for i in range(16))
N = 256
V = math.log(N, 2)
v = 160 * 192
print(v * V / 8 / 1024)
