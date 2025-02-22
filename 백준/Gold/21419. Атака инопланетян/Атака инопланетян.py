n = int(input())
tri = []
max_x = -1000000
max_y = -1000000
for _ in range(n):
    x, y, s = map(int, input().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    tri.append([x, y, s])

short_x = 10**20

for now_case in tri:
    x, y, s = now_case
    short_x = min(short_x, x + y + s - max_y - max_x)

if short_x > 0:
    print(f"{(short_x)**2/2:.3f}")
else:
    print(0)
