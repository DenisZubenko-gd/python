class MyZeroDevision(Exception):
    """Содственный класс исключения деления на ноль"""

    def __init__(self):
        self.error = 'Нельзя делить на ноль'


a = int(input('Первое число: '))
b = int(input('Второе число: '))

try:
    if b == 0:
        raise MyZeroDevision()
except:
    print(MyZeroDevision().error)
else:
    print(a / b)
