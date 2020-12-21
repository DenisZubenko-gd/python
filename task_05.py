"""Произведение четных сисел от 100 до 1000"""
from functools import reduce


def multiplication(prev_el, el):
    return prev_el * el


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(multiplication, my_list))
