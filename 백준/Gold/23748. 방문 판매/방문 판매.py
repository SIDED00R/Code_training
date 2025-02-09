N, X, Y = map(int, input().split())
INF = 10**9
dp = [[(INF, INF)] * (Y + 1) for _ in range(X + 1)]
dp[0][0] = (0, 0) 

for i in range(1, N + 1):
    xi, yi = map(int, input().split())
    new_dp = [row[:] for row in dp]
    for a in range(X + 1):
        for b in range(Y + 1):
            sales, last = dp[a][b]
            if sales < INF:
                na = min(X, a + xi) 
                nb = min(Y, b + yi) 
                candidate = (sales + 1, i)
                if candidate < new_dp[na][nb]:
                    new_dp[na][nb] = candidate
    dp = new_dp

min_sales, last_customer = dp[X][Y]
if min_sales == INF:
    print(-1)
else:
    print(min_sales)
    print(last_customer)
