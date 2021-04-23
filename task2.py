import math
from typing import Union, Any
from abc import ABC, abstractmethod


def convert_to_bin(number: int) -> str:
    res = ''
    while number > 0:
        res += str(number % 2)
        number //= 2
    return res[::-1]


def convert_to_bin_rev(number: str) -> int:
    res = 0
    div = len(number) - 1
    for bit in number:
        res += int(bit) * (2 ** div)
        div -= 1
    return res


def convert_to_nego(number: int) -> str:
    result = ''
    while number:
        remainder = number % -2
        number //= -2
        if remainder < 0:
            remainder += 2
            number += 1
        if remainder in (0, 1):
            result = f'{remainder}{result}'
    return result


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        if fib1 > n:
            break
        yield fib1


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = i * res
        if res > n:
            break
        yield res


def convert_fib(number) -> str:
    fib_list = list(fibonacci(number))
    fib_list.reverse()
    final_form = [0 for i in range(len(fib_list))]
    cur_dec = 0
    for fib_number in fib_list:
        if number >= fib_number:
            number -= fib_number
            final_form[cur_dec] += 1
        cur_dec += 1
    return ''.join(str(i) for i in final_form)


def convert_fact(number) -> str:
    fact_list = list(factorial(number))
    fact_list.reverse()
    final_form = [0 for i in range(len(fact_list))]
    cur_dec = 0
    for fact_number in fact_list:
        if number >= fact_number:
            final_form[cur_dec] += number // fact_number
            number %= fact_number
        cur_dec += 1
    return ''.join(str(i) for i in final_form)


def convert_fact_rev(number) -> int:
    razr = [int(i) for i in str(number)]
    fact_list = list(factorial(number))[:len(razr):]
    fact_list.reverse()
    return sum(map(lambda x, y: x * y, razr, fact_list))


def convert_fib_rev(number) -> int:
    razr = [int(i) for i in str(number)]
    fib_list = list(fibonacci(number))[:len(razr):]
    fib_list.reverse()
    return sum(map(lambda x, y: x * y, razr, fib_list))

