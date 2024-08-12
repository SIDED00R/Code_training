dp = [0] * 101
for idx in range(1, 101):
    dp[idx] = dp[idx - 1] + 1
    if idx >= 10:
        dp[idx] = min(dp[idx], dp[idx - 10] + 1)
    if idx >= 25:
        dp[idx] = min(dp[idx], dp[idx - 25] + 1)

t = int(input())
for _ in range(t):
    price = int(input())
    coin = 0
    while price:
        left = price % 100
        price //= 100
        coin += dp[left]
        
    print(coin)
    

