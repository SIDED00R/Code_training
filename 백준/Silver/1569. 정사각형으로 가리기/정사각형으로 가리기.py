n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

xs = [x for x, y in points]
ys = [y for x, y in points]

min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

dx = max_x - min_x
dy = max_y - min_y

if dx > dy:
    inner = [(x, y) for x, y in points if min_x < x < max_x]
    if not inner:
        print(dx)
    else:
        all_min_y = all(y == min_y for x, y in inner)
        all_max_y = all(y == max_y for x, y in inner)
        print(dx if (all_min_y or all_max_y) else -1)
elif dy > dx:
    inner = [(x, y) for x, y in points if min_y < y < max_y]
    if not inner:
        print(dy)
    else:
        all_min_x = all(x == min_x for x, y in inner)
        all_max_x = all(x == max_x for x, y in inner)
        print(dy if (all_min_x or all_max_x) else -1)
else:
    ok = all(
        x == min_x or x == max_x or y == min_y or y == max_y
        for x, y in points
    )
    print(dx if ok else -1)