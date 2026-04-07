n, l, w, h = map(int, input().split())

low = 0.0
high = min(l, w, h)

for _ in range(100):
    mid = (low + high) / 2
    total = int(l / mid) * int(w / mid) * int(h / mid)

    if total >= n:
        low = mid
    else:
        high = mid

print(high)