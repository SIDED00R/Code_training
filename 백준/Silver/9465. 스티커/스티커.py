import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0 for _ in range(n)] for _ in range(2) ]
    sticker = []
    for _ in range(2):
        line = list(map(int, input().rstrip('\n').split()))
        sticker.append(line)
    for i in range(n):
        if i == 0:
            dp[0][i] = sticker[0][i]
            dp[1][i] = sticker[1][i]
        elif i == 1:
            dp[0][i] = sticker[0][i] + dp[1][i - 1]
            dp[1][i] = sticker[1][i] + dp[0][i - 1]
        else:
            dp[0][i] = sticker[0][i] + max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] = sticker[1][i] + max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][-1], dp[1][-1]))        
    
    