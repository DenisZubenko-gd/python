"""Не очень понял как лучше реализовать задачу. Использовал yield и вывод результата как показано в задаче
По сути весь код один костыль"""


def fact(long: int):
    """Генератор вычислаяющий факториал
    :param long длинна значений"""

    for n in range(long):
        yield n + 1


long_fact = int(input('Введите длинну факториала, целое число: '))

f = 1
print_str = ''
for i in fact(long_fact):
    print_str = print_str + f' * {i}'
    f = f * i

print(f'{long_fact}! = {print_str[2:]} = {f}')
