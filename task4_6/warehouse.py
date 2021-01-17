"""Описан склад класса и методы работы с ним"""

from task4_6.validation import ValidCount, NegativeCount


class Warehouse:
    """Склад"""

    def __init__(self, location: str):
        self.location = location
        self.positions = dict()

    def __str__(self):
        return f'{self.location}: {self.positions}'

    def acceptance_of_goods(self, good, count):
        """Приём техники
        :param good товар
        :param count количество"""

        try:
            if type(count) != int:
                raise ValidCount
        except ValidCount as error:
            print(error)
            return
        self.positions[good] = int(count)
        print(f'На склад {self.location} добавлен товар {good}, количество {count}')

    @staticmethod
    def moving(warehouse_from, warehouse_in, good, count):
        """Перемещение между скаладами
        :param warehouse_from откуда перемещаем
        :param warehouse_in куда перемещаем
        :param good назначение
        :param count количество"""

        new_count_from_warehouse = warehouse_from.positions[good] - count
        try:
            if new_count_from_warehouse < 0:
                raise NegativeCount(warehouse_from.location)
        except NegativeCount as error:
            print(error)
            return
        if new_count_from_warehouse == 0:
            warehouse_from.positions.pop(good)
        else:
            warehouse_from.positions[good] = new_count_from_warehouse
        if good in warehouse_in.positions.keys():
            warehouse_in.positions[good] = warehouse_in.positions[good] + count
        else:
            warehouse_in.positions[good] = count
        print(f'Переместили из склада {warehouse_from.location} на склад {warehouse_in.location}: \n'
              f'{good} - {count}')
