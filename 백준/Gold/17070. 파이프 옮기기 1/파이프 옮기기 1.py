import sys
input = sys.stdin.readline

N = int(input())
# [0: horizon, 1: diagonal, 2: vertical]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

house = []
for _ in range(N):
    line = list(map(int, input().rstrip('\n').split()))
    house.append(line)

for i in range(N):
    for j in range(1, N):
        if i == 0 and j == 1:
            continue
        if house[i][j] != 1:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            if i != 0:
                dp[i][j][2] = dp[i - 1][j][2] + dp[i - 1][j][1] 
                if house[i - 1][j] != 1 and house[i][j - 1] != 1:
                    dp[i][j][1] = sum(dp[i - 1][j - 1])
print(sum(dp[-1][-1]))
        