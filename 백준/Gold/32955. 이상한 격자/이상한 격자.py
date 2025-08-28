def find(l, base, go, back):
    total = sum([(num - base) * back for num in l])
    now_total = total
    for idx, num in enumerate(l):
        if idx == 0:
            continue
        before_node = l[idx - 1]
        distance = num - before_node
        now_total = now_total + (distance * idx * go - distance * (len(l) - idx) * back)
        total = min(total, now_total)
    return total
n, a, b, c, d = map(int, input().split())
x_coordinates = []
y_coordinates = []
for _ in range(n):
    x, y = map(int, input().split())
    x_coordinates.append(x)
    y_coordinates.append(y)

x_coordinates = sorted(x_coordinates)
y_coordinates = sorted(y_coordinates)

print(find(x_coordinates, x_coordinates[0], b, a) + find(y_coordinates, y_coordinates[0], d, c))