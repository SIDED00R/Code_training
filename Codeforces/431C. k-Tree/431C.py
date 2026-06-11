MOD = 1000000007
n, k, d = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(k)]

for i in range(k):
    for j in range(n):
        if i >= j:
            matrix[i][j] = pow(2, j, MOD)
        else:
            matrix[i][j] = sum(matrix[i][j - i - 1:j]) % MOD
        
if d == 1:
    print(matrix[k - 1][n - 1])
else:
    ans = (matrix[k - 1][n - 1] - matrix[d - 2][n - 1])
    print(ans % MOD)