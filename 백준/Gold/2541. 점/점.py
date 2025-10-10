import sys

a, b = map(int, sys.stdin.readline().split())

def odd_part(x: int) -> int:
    x = abs(x)
    if x == 0:
        return 0
    while x % 2 == 0:
        x //= 2
    return x

d = b - a
d_odd = odd_part(d)

for _ in range(5):
    p, q = map(int, sys.stdin.readline().split())
    diff = q - p

    if d == 0:
        print('Y' if diff == 0 else 'N')
        continue

    if (d > 0 and diff <= 0) or (d < 0 and diff >= 0):
        print('N')
        continue

    print('Y' if (abs(diff) % d_odd == 0) else 'N')
