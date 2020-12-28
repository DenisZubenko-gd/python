class Road:
    """Дорога"""

    def __init__(self, length, width, mass_one=25, thickness=5):
        self._length = length
        self._width = width
        self._mass_one = mass_one
        self._thickness = thickness

    def mass_asphalt(self):
        """Расчет массы асфальта"""

        # Расчет идёт в КГ, сразу перевожу в тонны
        return int((self._length * self._width * self._mass_one * self._thickness) / 1000)


road = Road(20, 5000)
print(road.mass_asphalt())
