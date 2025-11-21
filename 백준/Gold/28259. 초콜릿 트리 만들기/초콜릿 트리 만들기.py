n, h, k = map(int, input().split())
line = list(map(int, input().split()))

dp = [[1e20 for _ in range(n)] for _ in range(h + 1)]

for idx in range(n):
    if idx in line:
        dp[0][idx] = 0
    else:
        dp[0][idx] = 1

for height in range(1, h + 1):
    for first in range(n):
        for second in range(first, n):
            total = first + second
            if 0 <= total < n:
                dp[height][total] = min(dp[height][total], dp[height - 1][first] + dp[height - 1][second] + dp[0][total])
            else:
                dp[height][total - n] = min(dp[height - 1][first] + dp[height - 1][second] + dp[0][total - n], dp[height][total - n])

print(min(dp[-1]))