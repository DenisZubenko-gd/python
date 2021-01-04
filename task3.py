class Cell:
    """Клетка"""

    def __init__(self, count_cell: int):

        self.count_cell = count_cell

    def __add__(self, other):
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        result = self.count_cell - other.count_cell
        if result < 0:
            print('Количество клеток отрицательное')
            return
        return Cell(result)

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __truediv__(self, other):
        return Cell((self.count_cell + other.count_cell) // 2)

    @staticmethod
    def make_order(cell, row_length):
        """Вывод ячейки по рядам
        :param cell клетка
        :param row_length длинна ряда"""

        for i in range(1, cell.count_cell + 1):
            if i % row_length == 0:
                print("*")
            else:
                print("*", end='')