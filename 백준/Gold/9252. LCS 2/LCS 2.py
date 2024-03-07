first = list(input())
second = list(input())
length = max(len(first), len(second))
dp = [["" for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            dp[i + 1][j + 1] = dp[i][j] + first[i]
        else:
            if len(dp[i][j + 1]) > len(dp[i + 1][j]):
                dp[i + 1][j + 1] = dp[i][j + 1]
            else:
                dp[i + 1][j + 1] = dp[i + 1][j]
                
if len(dp[-1][-1]):
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
else:
    print(0)