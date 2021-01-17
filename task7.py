class ComplexNumber:
    """Комплексное число"""

    def __init__(self, a: int, b: int):

        self.a = a
        self.b = b

    def __str__(self):
        if self.b >= 0:
            return f'{self.a} + {self.b}i'
        else:
            return f'{self.a} - {abs(self.b)}i'

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexNumber(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a - other.a
        new_b = self.b - other.b
        return ComplexNumber(new_a, new_b)

    def __mul__(self, other):
        new_a = (self.a * other.a) - (self.b * other.b)
        new_b = (self.a * other.b) + (self.b * other.a)
        return ComplexNumber(new_a, new_b)


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)
print(c1)
print(c2)
c3 = c1 + c2
print(c3)
c4 = c1 - c2
print(c4)
c5 = c1 * c2
print(c5)
