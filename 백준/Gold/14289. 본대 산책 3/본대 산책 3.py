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



n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1
d = int(input())
res = matpow(matrix, d)
print(res[0][0])