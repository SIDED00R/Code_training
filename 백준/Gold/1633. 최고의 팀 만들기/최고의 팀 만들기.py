stack = []
while True:
    try:
        w, b = map(int, input().split())
        stack.append([w, b])
    except:
        break

length = len(stack)
dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(length + 1)]
for k in range(length):
    b, w = stack[k]
    dp[k + 1][1][0] = max(dp[k][1][0], b)
    dp[k + 1][0][1] = max(dp[k][0][1], w)
    for i in range(16):
        for j in range(16):
            if dp[k][i][j] != 0:
                dp[k + 1][i][j] = max(dp[k][i][j], dp[k + 1][i][j])
                if i != 15:
                    dp[k + 1][i + 1][j] = max(dp[k + 1][i + 1][j], dp[k][i][j] + b)
                if j != 15:
                    dp[k + 1][i][j + 1] = max(dp[k + 1][i][j + 1], dp[k][i][j] + w)

print(dp[-1][-1][-1])