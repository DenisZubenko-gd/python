import time


class TrafficLight:
    """Светофор"""

    def __init__(self, color=''):
        self._color = color

    def running(self, count_cycle=1):
        """переключение светофора в режимы: красный, желтый, зеленый
        функция зациклена сама на себя
        :param count_cycle Количество циклов"""

        if count_cycle == 0:
            return

        self._color = 'Зеленый'
        print(self._color)
        time.sleep(7)

        self._color = 'Желтый'
        print(self._color)
        time.sleep(2)

        self._color = 'Красный'
        print(self._color)
        time.sleep(5)

        self.running(count_cycle - 1)


traffic = TrafficLight()
traffic.running(count_cycle=3)
