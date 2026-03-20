MOD = 1000000007

m, n, k = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]

port = {}
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    port[(y1, x1)] = (y2, x2)
    port[(y2, x2)] = (y1, x1)

start_dp = [[0] * m for _ in range(n)]

if matrix[0][0] != '1':
    start_dp[0][0] = 1

for y in range(n):
    for x in range(m):
        if matrix[y][x] == '1':
            continue
        if y == 0 and x == 0:
            continue

        val = 0
        if y > 0:
            val += start_dp[y - 1][x]
        if x > 0:
            val += start_dp[y][x - 1]

        start_dp[y][x] = val % MOD

end_dp = [[0] * m for _ in range(n)]

if matrix[n - 1][m - 1] != '1':
    end_dp[n - 1][m - 1] = 1

for y in range(n - 1, -1, -1):
    for x in range(m - 1, -1, -1):
        if matrix[y][x] == '1':
            continue
        if y == n - 1 and x == m - 1:
            continue

        val = 0
        if y + 1 < n:
            val += end_dp[y + 1][x]
        if x + 1 < m:
            val += end_dp[y][x + 1]

        end_dp[y][x] = val % MOD

answer = start_dp[n - 1][m - 1]

for (y, x), (ny, nx) in port.items():
    if matrix[y][x] != 'P':
        continue
    if (ny, nx) == (y, x + 1) or (ny, nx) == (y + 1, x):
        continue

    answer += start_dp[y][x] * end_dp[ny][nx]
    answer %= MOD

print(answer % MOD)