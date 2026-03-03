n, m, a, b = map(int, input().split())
total = (n * 3 - m) * a
if total > 0:
    print(total + b)
else:
    print(0)