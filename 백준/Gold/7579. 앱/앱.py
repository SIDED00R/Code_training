import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip('\n').split())
active = list(map(int, input().rstrip('\n').split()))
disable = list(map(int, input().rstrip('\n').split()))
total_disable = sum(disable)
dp = [[0 for _ in range(total_disable + 1)] for _ in range(N + 1)]

answer = 1e9
for i in range(1, N + 1):
    active_memory = active[i - 1]
    disable_cost = disable[i - 1]
    for j in range(total_disable + 1):
        if j >= disable_cost:
            dp[i][j] = max(dp[i - 1][j - disable_cost] + active_memory, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
        if dp[i][j] >= M:
            answer = min(answer, j)
            
print(answer)
            