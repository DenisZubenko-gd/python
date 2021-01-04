class Clothes:
    """Одежда"""

    def __init__(self, size: int, type_clothes: str):
        self.size = size
        self.type_clothes = type_clothes

    @property
    def tissue_consumption(self):
        if self.type_clothes == 'пальто':
            return round(self.size/6.5 + 0.5, 2)
        elif self.type_clothes == 'костюм':
            return round(2 * self.size + 0.3, 2)
        else:
            return 'Нет задан такой тип одежды'


a = Clothes(10, 'пальто')
print(a.tissue_consumption)
b = Clothes(3, 'костюм')
print(b.tissue_consumption)