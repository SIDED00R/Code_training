MOD = 10**9 + 7

p, c, k = map(int, input().split())
M = list(map(int, input().split()))

base = [0] * (p + 1)
for i in range(1, p):
    base[i] = M[i] - M[i - 1]

dp = 0
pw = c
for i in range(p - 1, 0, -1):
    dp += pw * base[i]
    pw *= c
base[p] = -dp

if k <= p:
    ans = abs(base[k]) % MOD
else:
    if k % p == 0:
        start = p
        t = k // p - 1
    else:
        start = k % p
        t = k // p

    ans = abs(base[start]) % MOD
    ans = ans * pow(c, p * t, MOD) % MOD

print(ans)