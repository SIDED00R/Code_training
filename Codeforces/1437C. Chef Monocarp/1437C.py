def solve(n, t):
    t.sort()
    INF = float('inf')
    dp = [0] + [INF] * n
    for T in range(1, 2 * n + 1):
        for j in range(min(T, n), 0, -1):
            if dp[j - 1] != INF:
                dp[j] = min(dp[j], dp[j - 1] + abs(T - t[j - 1]))
    return dp[n]

q = int(input())
for _ in range(q):
    n = int(input())
    time_list = sorted(list(map(int, input().split())))
    print(solve(len(time_list), time_list))