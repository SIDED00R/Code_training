x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    num = (z + 1) * x - 100 * y
    den = 100 - (z + 1)
    print((num + den - 1) // den)