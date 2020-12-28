class Car:
    """Машина"""

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """Запуск машины"""

        print('Машина поехала')

    def stop(self):
        """Остановка машины"""

        print('Машина остановилась')

    def turn(self, direction):
        """Поворот машины
        :param direction Налево, Направо"""

        print(f'Машина повернула {direction}')

    def show_speed(self):
        """Показать Скорость"""

        print(f'Скорость {self.speed}')


class TownCar(Car):
    """Городская машина"""

    def show_speed(self):
        """Показать Скорость"""

        print(f'Скорость {self.speed}')
        if self.speed > 60:
            print('Скорость превышена')


class SportCar(Car):
    """Спортиваня машина"""

    pass


class WorkCar(Car):
    """Рабочая машина"""

    def show_speed(self):
        """Показать Скорость"""

        print(f'Скорость {self.speed}')
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):
    """Полицейская машина"""

    pass


town_car = TownCar(70, 'Черная', 'Fudi', False)
town_car.go()
town_car.turn('Налево')
town_car.turn('Направо')
town_car.show_speed()
town_car.stop()
