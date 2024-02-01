import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().rstrip('\n').split()))
    if i == 0:
        dp[0][0] = line[0]
        continue
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = line[j] + dp[i - 1][j]
        elif j == i:
            dp[i][j] = line[j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = line[j] + max(dp[i - 1][j], dp[i - 1][j - 1])
            
print(max(dp[-1]))