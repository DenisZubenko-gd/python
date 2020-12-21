from sys import argv


def wage_func(hours: str, rate: str, prize: str):
    """Расчте заработной платы
    :param hours отработнные часы
    :param rate ставка в час
    :param prize премия"""

    return int(hours) * int(rate) + int(prize)


script_name, hours, rate, prize = argv
wage = wage_func(hours, rate, prize)
print(f'Заработная плата {wage} руб.')
