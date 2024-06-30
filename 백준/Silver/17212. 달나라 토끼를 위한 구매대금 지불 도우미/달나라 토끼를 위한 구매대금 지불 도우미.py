n = int(input())

dp = [0 for _ in range(n + 1)]
dp[0] = 0

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    for case in [2, 5, 7]:
        if i - case >= 0:
            dp[i] = min(dp[i], dp[i - case] + 1)
            
print(dp[-1])