import sys
input = sys.stdin.readline

def matrix_mul(matrixA, matrixB):
    n = len(matrixA)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += matrixA[i][k] * matrixB[k][j]
                new_matrix[i][j] %= 1000
    return new_matrix

def matrix_devide(matrix, B):
    n = len(matrix)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    if B == 1:
        return matrix
    elif B == 2:
        return matrix_mul(matrix, matrix)
    else:
        d_matrix = matrix_devide(matrix, B // 2)
        answer = matrix_mul(d_matrix, d_matrix)
        if B % 2:
            return matrix_mul(matrix, answer)
        else:
            
            return answer

N, B = map(int, input().rstrip('\n').split())
matrix = []
for _ in range(N):
    row = list(map(int, input().rstrip('\n').split()))
    matrix.append(row)
    
for line in matrix_devide(matrix, B):
    for num in line:
        print(num % 1000, end = " ")
    print()