from task2 import convert_fib, convert_to_bin, convert_to_bin_rev
from typing import Tuple
import math


def un_code(number: int, code_type: str = "direct") -> str:
    res = ''
    number_type = {'inverse': '0', 'direct': '1'}
    for i in range(number):
        res += number_type[code_type]
    if code_type == 'inverse':
        return res + '1'
    else:
        return res + '0'


def fib_code(number: int) -> str:
    return convert_fib(number)[::-1] + '1'


def gamma_lev(number: int) -> str:
    bin_form = convert_to_bin(number)[::-1]
    tmp = ''
    for i in range(len(bin_form) - 1):
        tmp += f'0{bin_form[i]}'
    return tmp + bin_form[-1]


def get_limits(number: int) -> Tuple[int, int]:
    min_l = 0
    max_l = 1
    while True:
        if (number >= 2 ** min_l) and (number <= 2 ** max_l - 1):
            return tuple((min_l, max_l))
        else:
            min_l += 1
            max_l += 1


def gamma_el(number: int) -> str:
    limits = get_limits(number)
    return un_code(limits[0], 'inverse') + convert_to_bin(int(number - 2 ** limits[0]))


def del_el(number: int) -> str:
    bin_form = convert_to_bin(number)
    l = len(bin_form)
    l_bin = convert_to_bin(int(l))
    m = len(l_bin)
    return '0' * (m - 1) + '1' + l_bin[1::] + bin_form[1::]


def omega_el(number: int) -> str:
    res = '0'
    while number != 1:
        bin_form = convert_to_bin(number)
        res = bin_form + res
        number = len(bin_form) - 1
    return res


def golomb(number: int, m: int) -> str:
    if m // 2 == 0:
        pass
    else:
        pass


def exp_golomb(number: int, m: int) -> str:
    w = int(math.floor(1 + (number // (2 ** m))))
    f = int(math.floor(math.log(w, 2)))
    tmp_bin = convert_to_bin(number)
    print(w, f, tmp_bin)
    if len(tmp_bin) < m:
        tmp_bin = ('0' * (m - len(tmp_bin))) + tmp_bin
    return un_code(f) + convert_to_bin(w)[-f:] + tmp_bin[-m:]


print(gamma_el(100))
print(omega_el(15))
print(del_el(34))

