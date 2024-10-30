import math

def determinant_5x5(matrix):
    def minor(matrix, row, col):

        return [
            [matrix[i][j] for j in range(len(matrix)) if j != col]
            for i in range(len(matrix)) if i != row
        ]

    def determinant(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for col in range(len(matrix)):
            sign = (-1) ** col
            det += sign * matrix[0][col] * determinant(minor(matrix, 0, col))
        return det

    return determinant(matrix)

def tetrahedron_volume_no_numpy(num):
    d12, d13, d14, d23, d24, d34 = num
    CM = [
        [0, 1, 1, 1, 1],
        [1, 0, d12**2, d13**2, d14**2],
        [1, d12**2, 0, d23**2, d24**2],
        [1, d13**2, d23**2, 0, d34**2],
        [1, d14**2, d24**2, d34**2, 0]
    ]

    determinant = determinant_5x5(CM)

    volume = math.sqrt(abs(determinant) / 288)

    return volume

num = list(map(int, input().split()))
volume_example = tetrahedron_volume_no_numpy(num)
print(round(volume_example, 4))