"""итератор, повторяющий элементы некоторого списка, определенного заранее.
Список формируется случайными значениями.
В скрипт передается начальное и конечное значения, длинна и кол-во повторений"""
from sys import argv
from itertools import cycle
from random import randint

script_name, first_number, last_number, long, end_cycle = argv


def generate_list(first_number, last_number, long):
    for i in range(long):
        yield randint(first_number, last_number)


c = 0
for el in cycle(generate_list(int(first_number), int(last_number), int(long))):
    if c > int(end_cycle):
        break
    print(el, end=' ')
    c += 1
