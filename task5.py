class Stationery:
    """Канцелярские принадлежности"""

    def __init__(self, title: str):
        self.title = title

    def drow(self):
        """Отрисовка"""

        print('Запуск отрисовки.')


class Pen(Stationery):

    def drow(self):
        """Отрисовка"""

        print('Запись ручкой')


class Pencil(Stationery):

    def drow(self):
        """Отрисовка"""

        print('Чертеж карандашом')


class Handle(Stationery):

    def drow(self):
        """Отрисовка"""

        print('Отметка маркером')


pen = Pen('Ручка')
pen.drow()
pencil = Pencil('Карандащ')
pencil.drow()
handle = Handle('Маркер')
handle.drow()
