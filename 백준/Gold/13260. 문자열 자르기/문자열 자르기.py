import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cuts = list(map(int, input().split()))
cuts = [0] + sorted(cuts) + [n]
size = len(cuts)

dp = [[0] * size for _ in range(size)]

for length in range(2, size):
    for i in range(size - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i + 1, j):
            cost = dp[i][k] + dp[k][j] + (cuts[j] - cuts[i])
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][size - 1])
