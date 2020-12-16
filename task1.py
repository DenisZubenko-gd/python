def division(divident: int, divider: int):
    """Делит первое число на второе
    :param divident делимое
    :param divider делитель
    :return result результат операции"""

    result = divident / divider

    return result


# Ввод значений для примера
num1 = int(input('Введите делимое: '))
num2 = int(input('Введите делитель: '))

try:
    print(f"{num1}/{num2}={division(num1, num2)}")
except ZeroDivisionError:
    print('Нельзя делить на ноль')
