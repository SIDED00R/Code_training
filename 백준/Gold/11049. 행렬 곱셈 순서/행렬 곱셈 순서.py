import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
    
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        min_value = 0
        for idx in range(i - j):
            now = dp[j + idx][j] + dp[i][j + idx + 1] + matrix[j][0] * matrix[j + idx][1] * matrix[i][1]
            if min_value == 0:
                min_value = now
            elif min_value > now:
                min_value = now
        dp[i][j] = min_value
print(dp[-1][0])