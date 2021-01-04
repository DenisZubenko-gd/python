class Matrix:
    """Матрица"""

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for str in self.matrix:
            for i in str:
                str_matrix = str_matrix + f'{i} '
            str_matrix = str_matrix + '\n'
        return str_matrix

    def __add__(self, other):
        new_matrix = []
        for sublist in zip(self.matrix, other.matrix):
            new_str = []
            for numbers in zip(sublist[0], sublist[1]):
                new_str.append(sum(numbers))
            new_matrix.append(new_str)
        return Matrix(new_matrix)


m1 = Matrix([[1, 2, 3], [3, 2, 1]])
m2 = Matrix([[1, 2, 3], [3, 2, 1]])
print(m1 + m2)
