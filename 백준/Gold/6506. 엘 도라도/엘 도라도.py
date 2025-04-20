while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    line = list(map(int, input().split()))
    
    dp = [[0 for _ in range(n)] for _ in range(k)]
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, k):
        for j in range(n):
            for idx in range(j):
                if line[idx] < line[j]:
                    dp[i][j] += dp[i - 1][idx]

    print(sum(dp[-1]))
