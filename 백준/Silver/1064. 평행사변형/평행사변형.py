def l(xa, ya, xb, yb):
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    
xa, ya, xb, yb, xc, yc = map(int, input().split())

if (yb - ya) * (xc - xb) - (yc - yb) * (xb - xa) == 0:
    print(-1)
    exit()

f = l(xa, ya, xb, yb)
s = l(xa, ya, xc, yc)
t = l(xb, yb, xc, yc)
print((max(f, s, t) - min(f, s, t)) * 2)