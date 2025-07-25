n, m = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if sum(num_list[i:]) + (n - i - 1) <= m:
        dp[i] = 0
        continue
    dp[i] = dp[i + 1] + (m - num_list[i]) ** 2
    count = 1
    while True:
        if i + count >= n:
            break
        now_total = 0
        for idx in range(count + 1):
            now_total += num_list[i + idx]
        if now_total + count > m:
            break
        else:
            dp[i] = min(dp[i], dp[i + count + 1] + (m - now_total - count) ** 2)
            count += 1
print(dp[0])