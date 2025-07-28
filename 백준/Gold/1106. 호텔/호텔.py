import math

c, n = map(int, input().split())
dp = [[1e9 for _ in range(c + 1)] for _ in range(n + 1)]
stack = [[0, 0]]
for _ in range(n):
    cost, people = map(int, input().split())
    stack.append([cost, people])

for i in range(1, n + 1):
    cost, people = stack[i]
    for j in range(c + 1):
        dp[i][j] = math.ceil(j / people) * cost
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        if j - people >= 0:
            dp[i][j] = min(dp[i][j - people] + cost, dp[i][j], dp[i - 1][j - people] + cost)

print(dp[-1][-1])
            