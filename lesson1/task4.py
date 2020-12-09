"""Определяем самое большую цифру в числе"""

my_number = input('Введите положительное целое число: ')

if len(my_number) == 1:
    print(f'Самое большое число: {my_number}')
else:
    max_number = my_number[0]
    for i in my_number[1:]:
        max_number = i if int(i) > int(max_number) else max_number
    print(f'Самое большое число: {max_number}')
