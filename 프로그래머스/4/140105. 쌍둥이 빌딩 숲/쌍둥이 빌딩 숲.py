MOD = 1000000007

def solution(n, count):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j] * (i - 1) * 2 + dp[i - 1][j - 1]) % MOD
                
    return dp[n][count]