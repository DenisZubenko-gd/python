class Worker:
    """Работник"""

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    """Должность"""

    def get_full_name(self):
        """Полное имя"""

        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """Доход с учетом премии"""

        return self._income.get('wage') + self._income.get('bonus')


position = Position('Иван', 'Иванов', 'Программист', 40000, 15000)
print(position.get_full_name())
print(position.get_total_income())
