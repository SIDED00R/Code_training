n = int(input())
line = list(map(int, input().split()))
dp = [[0, 0, 0, 0] for _ in range(n + 1)]

dp[1][0] = line[0]
dp[1][1] = line[0] * 2
dp[2][0] = dp[1][0] + line[1]
dp[2][1] = dp[1][0] + 2 * line[1]
dp[2][2] = dp[1][1] + 2 * line[1]
dp[3][0] = dp[2][0] + line[2]
dp[3][1] = dp[2][0] + 2 * line[2]
dp[3][2] = dp[2][1] + 2 * line[2]
dp[3][3] = dp[2][2] + 2 * line[2]
    

for idx in range(4, n + 1):
    dp[idx][0] = max(dp[idx - 1][0], dp[idx - 1][3]) + line[idx - 1]
    dp[idx][1] = max(dp[idx - 1][0], dp[idx - 1][3]) + 2 * line[idx - 1]
    dp[idx][2] = dp[idx - 1][1] + 2 * line[idx - 1]
    dp[idx][3] = dp[idx - 1][2] + 2 * line[idx - 1]

print(max(dp[-1]))
