class Date:
    """Дата"""

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_int(cls, date: str):
        """Строковую дату в число
        :param date дата день-месяц-год
        :return day, month, year день, месяц, год"""

        day, month, year = map(int, date.split('-'))

        return day, month, year

    @staticmethod
    def is_month_valid(date):
        """Проверка валидность месяца
        :param date дата день-месяц-год"""

        day, month, year = map(int, date.split('-'))
        return month <= 12


print(Date.date_int('13-01-2021'))
print(Date.is_month_valid('13-21-2021'))
