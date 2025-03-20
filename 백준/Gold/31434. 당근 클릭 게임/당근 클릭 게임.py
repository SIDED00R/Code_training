n, k = map(int, input().split())

carrot = []
max_s = 0
for _ in range(n):
    a, b = map(int, input().split())
    carrot.append([a, b])
    max_s = max(max_s, b)

carrot.sort()

dp = [[-1 for _ in range(max_s * (n + 1) + 1)] for _ in range(k + 1)]
dp[0][1] = 0
for i in range(k):
    for j in range(max_s * n + 1):
        if dp[i][j] != -1:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + j)
        else:
            continue
        for carrot_case in carrot:
            a, b = carrot_case
            if dp[i][j] >= a:
                dp[i + 1][j + b] = max(dp[i + 1][j + b], dp[i][j] - a)
            else:
                break


print(max(dp[-1]))

