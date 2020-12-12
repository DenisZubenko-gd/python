"""Обмен значений внутри списка"""

my_list = input('Введи значения списка через пробел: ').split(' ')

for i in range(len(my_list)):
    if i % 2 == 1:
        my_list[i], my_list[i -1] = my_list[i - 1], my_list[i]

print(' '.join(my_list))