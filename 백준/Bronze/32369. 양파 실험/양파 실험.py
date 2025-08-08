n, a, b = map(int, input().split())
good = 1
bad = 1
for _ in range(n):
    good += a
    bad += b
    good, bad = max(good, bad), min(good, bad)
    if good == bad:
        bad -= 1
    
print(good, bad)