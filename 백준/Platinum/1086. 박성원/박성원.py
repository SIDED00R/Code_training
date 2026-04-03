import math
from math import gcd

def simplify_fraction(a, b):
    g = gcd(a, b)
    return a // g, b // g

n = int(input())
nums = [input().strip() for _ in range(n)]
k = int(input())

lengths = [len(x) for x in nums]
mods = [int(x) % k for x in nums]

max_len = max(lengths)
pow10 = [1] * (max_len + 1)
for i in range(1, max_len + 1):
    pow10[i] = (pow10[i - 1] * 10) % k

trans = [[0] * k for _ in range(n)]
for i in range(n):
    p = pow10[lengths[i]]
    m = mods[i]
    for r in range(k):
        trans[i][r] = (r * p + m) % k

dp = [[0] * k for _ in range(1 << n)]
dp[0][0] = 1

for mask in range(1 << n):
    for r in range(k):
        if dp[mask][r] == 0:
            continue
        cur = dp[mask][r]
        for i in range(n):
            if mask & (1 << i):
                continue
            nxt = mask | (1 << i)
            nr = trans[i][r]
            dp[nxt][nr] += cur

num = dp[(1 << n) - 1][0]
den = math.factorial(n)
a, b = simplify_fraction(num, den)
print(f"{a}/{b}")