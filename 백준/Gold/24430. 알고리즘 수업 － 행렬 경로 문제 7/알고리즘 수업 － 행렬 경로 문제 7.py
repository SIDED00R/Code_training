import sys

n = int(input())
matrix = [[[0, 0] for _ in range(n)] for _ in range(n)]
dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        matrix[i][j][0] = line[j]

p = int(input())
for _ in range(p):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1][1] += 1

dp[0][0] = matrix[0][0]
for i in range(n):
    if i == 0:
        for j in range(1, n):
            dp[0][j] = [dp[0][j - 1][0] + matrix[i][j][0], dp[0][j - 1][1] + matrix[i][j][1]]
    for j in range(n):
        if j == 0:
            dp[i][j] = [dp[i - 1][j][0] + matrix[i][j][0], dp[i - 1][j][1] + matrix[i][j][1]]
        else:
            if dp[i - 1][j][0] > dp[i][j - 1][0]:
                dp[i][j] = [dp[i - 1][j][0] + matrix[i][j][0], dp[i - 1][j][1] + matrix[i][j][1]]
            elif dp[i - 1][j][0] < dp[i][j - 1][0]:
                dp[i][j] = [dp[i][j - 1][0] + matrix[i][j][0], dp[i][j - 1][1] + matrix[i][j][1]]
            else:
                dp[i][j] = [dp[i - 1][j][0] + matrix[i][j][0], max(dp[i - 1][j][1], dp[i][j - 1][1]) + matrix[i][j][1]]

print(dp[-1][-1][0], dp[-1][-1][1])