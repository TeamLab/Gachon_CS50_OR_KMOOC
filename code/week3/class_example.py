class Matrix(object):
    def __init__(self, matrix_list=None):
        if matrix_list is not None:
            self.matrix_list = matrix_list

    def __add__(self, other):
        if isinstance(other, Matrix):
            result = [[sum(row) for row in zip(*t)] for t in zip(self.matrix_list, other.matrix_list)]
            return result
        else:
            raise TypeError

    def __str__(self):
        return str(self.matrix_list)

matrix_list_a = [[3, 6], [4, 5]]
mat_x = Matrix(matrix_list_a)
print(mat_x)

matrix_list_b = [[5, 8], [6, 7]]
mat_y = Matrix(matrix_list_a)
print(mat_x + mat_y)