"""Описаны классы оргтехники"""


class OfficeEquipment:
    """Оргтехница"""

    def __init__(self, price: float, destination: str):
        """
        :param price: цена
        :param destination: назначение
        """

        self.price = price
        self.destination = destination


class Printer(OfficeEquipment):
    """Принтер"""

    def __init__(self, price: float, destination: str, speed: int, color: bool):
        """
        :param price: цена
        :param destination: назначение
        :param speed: скорость печати
        :param color: цветность
        """

        super().__init__(price, destination)
        self.speed = speed
        self.color = color


class Scanner(OfficeEquipment):
    """Сканер"""

    def __init__(self, price: float, destination: str, height: int, width: int, interface: str):
        """
        :param price: цена
        :param destination: назначение
        :param height: Высота разрешения
        :param width: ширина разрешения
        :param interface: интерфейс
        """

        super().__init__(price, destination)
        self.resolution = f"{height}x{width}"
        self.interface = interface


class Xerox(OfficeEquipment):
    """Ксерокс"""

    def __init__(self, price: float, destination: str, auto_feed: bool, technology: str):
        """
        :param price: цена
        :param destination: назначение
        :param auto_feed: Автоподача
        :param technology: Технология печати
        :param interface: интерфейс
        """

        super().__init__(price, destination)
        self.auto_feed = auto_feed
        self.technology = technology