n, m = map(int, input().split())
time_list = []
dp = [[-1 for _ in range(m + 2)] for _ in range(n + 1)]
for _ in range(n):
    time_list.append(int(input()))

dp[0][0] = 0
for i in range(n):
    for j in range(m + 1):
        if dp[i][j] != -1:
            rest_j = j
            if rest_j == 0:
                dp[i + 1][0] = max(dp[i][j], dp[i + 1][0])
            if i + rest_j <= n:
                dp[i + rest_j][0] = max(dp[i][j], dp[i + rest_j][0])
            try:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + time_list[i])
            except:
                continue
print(dp[-1][0])