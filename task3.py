class IsNumber(Exception):
    """Исключение на проверку число"""

    def __init__(self):
        self._error_txt = 'Вы ввели не число'

    def __str__(self):
        return self._error_txt


def input_list():
    """Формирование списка чисел пользователем"""

    my_list = []

    while True:
        number = input('Введите число (для остановки введите stop): ')
        if number == 'stop':
            break
        else:
            try:
                if not number.isdigit():
                    raise IsNumber()
            except IsNumber as error:
                print(error)
                continue
            my_list.append(int(number))
    return my_list


print(input_list())