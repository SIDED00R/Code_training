import sys
n = int(sys.stdin.readline().strip())
r = n // 2
x = r
t = 1
# factor 2
while x % 2 == 0:
    x //= 2
p = 3
while p * p <= x:
    if x % p == 0:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if p % 4 == 1:
            t *= (2 * e + 1)
    p += 2
# remaining prime
if x > 1 and x % 4 == 1:
    t *= 3  # exponent 1 -> (2*1+1)
ans = 8 * r - 4 * t
print(ans)
