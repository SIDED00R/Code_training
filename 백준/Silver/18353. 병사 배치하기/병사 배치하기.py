n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
line = list(map(int, input().split()))
dp[0][0] = line[0]
for idx in range(1, n):
    now_num = line[idx]
    dp[idx][0] = max(dp[idx - 1][0], now_num)
    for now_idx in range(1, n):
        dp[idx][now_idx] = dp[idx - 1][now_idx]
        if dp[idx][now_idx] == 0:
            if dp[idx][now_idx - 1] > now_num:
                dp[idx][now_idx] = now_num
            break
        else:
            if dp[idx][now_idx - 1] > now_num and dp[idx][now_idx] < now_num:
                dp[idx][now_idx] = now_num

for idx, num in enumerate(dp[-1]):
    if num != 0:
        answer = idx

print(n - answer - 1)