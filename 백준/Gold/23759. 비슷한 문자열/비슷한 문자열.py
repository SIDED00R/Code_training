n, k = map(int, input().split())
check = {i: {chr(idx + 97): -1 for idx in range(26)} for i in range(k)}
dp = [[-1 for _ in range(k)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(k):
        alp = line[j]
        dp[i][j] = check[j][alp]
        check[j][alp] = i

answer = [[-1, -1] for _ in range(n + 1)]
for i in range(1, n + 1):
    answer[i][1] = max(answer[i - 1])
    now_max = 1
    for j in range(k):
        before_idx = dp[i - 1][j] + 1
        if before_idx == -1:
            continue
        now_max = max(now_max, answer[before_idx][0] + 1)
    answer[i][0] = now_max

print(n - max(answer[-1]))