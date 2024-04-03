import sys
input = sys.stdin.readline

N = int(input()) 
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(1 << 10):
            if j > 0:
                dp[i][j][k | (1 << j)] += dp[i-1][j-1][k]
            if j < 9:
                dp[i][j][k | (1 << j)] += dp[i-1][j+1][k]
            dp[i][j][k | (1 << j)] %= 1e9
            
answer = 0
for j in range(10):
    answer += dp[N][j][(1 << 10) - 1]
    answer %= 1e9
print(int(answer))