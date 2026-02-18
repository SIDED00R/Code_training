def matrix_multiply(A, B):
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]), (A[0][0]*B[0][1] + A[0][1]*B[1][1])],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]), (A[1][0]*B[0][1] + A[1][1]*B[1][1])]]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    matrix = [[1, 1], [1, 0]]
    power_matrix = matrix_power(matrix, n - 1)
    return power_matrix[0][0]

n = int(input())
print(fibonacci(n))
