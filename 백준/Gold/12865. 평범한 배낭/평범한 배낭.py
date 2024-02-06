import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip('\n').split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = map(int, input().rstrip('\n').split())
    for j in range(1, K + 1):
        if W <= j:
            dp[i][j] = max(dp[i - 1][j - W] + V, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
                
print(dp[-1][-1])