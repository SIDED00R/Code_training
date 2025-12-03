import sys
input = sys.stdin.readline
MOD = 10**9 + 7

W, L = map(int, input().split())
M = L - 2 

dp = [[0] * 4 for _ in range(M + 1)]
ndp = [[0] * 4 for _ in range(M + 1)]

for x in range(M + 1):
    s = 0
    if x == 0:
        s |= 1
    if x == M:
        s |= 2
    dp[x][s] = 1

for _ in range(2, W + 1):
    for x in range(M + 1):
        for s in range(4):
            ndp[x][s] = 0

    for x in range(M + 1):
        for s in range(4):
            cur = dp[x][s]
            if not cur:
                continue
            for d in (-1, 0, 1):
                nx = x + d
                if 0 <= nx <= M:
                    ns = s
                    if nx == 0:
                        ns |= 1
                    if nx == M:
                        ns |= 2
                    ndp[nx][ns] = (ndp[nx][ns] + cur) % MOD
    dp, ndp = ndp, dp

ans = 0
for x in range(M + 1):
    ans = (ans + dp[x][3]) % MOD

print(ans)
