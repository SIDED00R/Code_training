MOD = 1000000007

def perm_mod(n, k):
    if k > n:
        return 0
    res = 1
    for i in range(k):
        res = res * (n - i) % MOD
    return res

def comb_mod(n, k):
    if k < 0 or k > n:
        return 0
    numerator = perm_mod(n, k)
    denominator = 1
    for i in range(1, k + 1):
        denominator = denominator * i % MOD
    return numerator * pow(denominator, MOD - 2, MOD) % MOD

n, l, r = map(int, input().split())
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
    
for i in range(1, n):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i - 1][j] * i % MOD
            continue
        total = 0
        for idx in range(i):
            total += dp[i - idx - 1][j - 1] * perm_mod(i, idx) % MOD
        dp[i][j] = total % MOD

n -= 1
l -= 1
r -= 1

answer = 0
if l == 0 and r == 0:
    if n == 0:
        print(1)
    else:
        print(0)
else:
    left = n - l - r
    for i in range(left + 1):
        answer += comb_mod(n, l + i) * dp[l + i - 1][l - 1] * dp[r + left - i - 1][r - 1] % MOD
    print(answer % MOD)
    
