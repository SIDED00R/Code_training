def solution(matrix_sizes):
    N = len(matrix_sizes)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i - 1, -1, -1):
            min_value = 0
            for idx in range(i - j):
                now = dp[j + idx][j] + dp[i][j + idx + 1] + matrix_sizes[j][0] * matrix_sizes[j + idx][1] * matrix_sizes[i][1]
                if min_value == 0:
                    min_value = now
                elif min_value > now:
                    min_value = now
            dp[i][j] = min_value
    return dp[N - 1][0]