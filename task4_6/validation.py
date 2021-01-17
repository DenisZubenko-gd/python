"""Описаны методы """


class ValidCount(Exception):
    """Валидация количества техники"""

    def __init__(self):
        self.txt = 'Количество должен быть числом.'

    def __str__(self):
        return self.txt


class NegativeCount(Exception):
    """Валидация отрицательного количество"""

    def __init__(self, warehouse):
        self.txt = f'У склада {warehouse} возникает отрицательный остаток. Операция отменена'

    def __str__(self):
        return self.txt
