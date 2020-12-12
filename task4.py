"""Вывод слов из списка с укзание индекса"""

in_str = input('Вводите слова через пробел: ')

for i, el in enumerate(in_str.split(' '), 1):
    if len(el) > 10:
        el = el[:10]
    print(f'{i}: {el}')