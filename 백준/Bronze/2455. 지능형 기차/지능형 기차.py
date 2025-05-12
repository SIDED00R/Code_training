ans = 0
total = 0
for _ in range(4):
    a, b = map(int, input().split())
    total += (b - a)
    ans = max(ans, total)

print(ans)