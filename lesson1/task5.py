"""Определение рентабельности фирмы"""

proceeds = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

if proceeds > costs:
    print('Фирма поручает прибыль')
    #вот здесь не понял про рентабельность как она вычесляется, поэтому просто поделил и округлил
    print(f'Рентабельность фирмы {round(proceeds/costs, 2)}')
    employees = int(input('Сколько работает сотрудников на фирму? '))
    print(f'На кождого сотрудника выходит по {proceeds//employees} рублей')
elif proceeds < costs:
    print('Фирма теряет деньги')
elif proceeds == costs:
    print('Фирма работает в ноль')