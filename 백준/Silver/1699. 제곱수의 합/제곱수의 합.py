n = int(input())
dp = [0] * (n + 1)
for idx in range(1, n + 1):
    dp[idx] = dp[idx - 1] + 1
    for num in range(1, 1001):
        if idx - num ** 2 >= 0:
            dp[idx] = min(dp[idx], dp[idx - num ** 2] + 1)
        else:
            break
        
print(dp[n])
