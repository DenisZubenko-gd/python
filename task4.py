def my_func1(x: int, y: int):
    """Возведение в отрицательную степень использую математическую операцию
    :param x число
    :param y степень"""

    result = 1/x ** abs(y)

    return result


def my_func2(x: int, y: int):
    """Возведение в отрицательную степень использую цикл
    :param x число
    :param y степень
    :return result"""

    m = 1
    for i in range(0, abs(y)):
        m *= x
    result = 1/m

    return result


print(my_func1(2, -3))
print(my_func2(2, -3))
