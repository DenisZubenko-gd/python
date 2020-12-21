"""Итератор, генерирующий целые числа, начиная и заканчивая с указанноых"""
from sys import argv
from itertools import count

script_name, first_number, last_number = argv

for i in count(int(first_number)):
    if i > int(last_number):
        break
    print(i, end=' ')
