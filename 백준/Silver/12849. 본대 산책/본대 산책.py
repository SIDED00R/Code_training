def matmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            C[i][j] = total % 1000000007
    return C

def matpow(A, power):
    n = len(A)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    while power > 0:
        if power % 2 == 1:
            result = matmul(result, A)
        A = matmul(A, A)
        power //= 2
    return result

matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

n = int(input())
res = matpow(matrix, n)
print(res[0][0])