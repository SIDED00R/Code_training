from collections import defaultdict

n = int(input())

dp = [defaultdict(int) for _ in range(n + 3)]
dp[0][0] = 0
for i in range(n):
    for k, v in dp[i].items():
        dp[i + 1][k] = max(v + 1, dp[i + 1][k], v + k)
        dp[i + 2][v] = max(dp[i + 2][v], v)

answer = 0
for k, v in dp[n].items():
    answer = max(answer, v)

print(answer)