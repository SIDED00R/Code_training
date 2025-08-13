n = int(input())
x_list = [0 for _ in range(1000001)]
y_list = [0 for _ in range(1000001)]
for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    min_x = min(x1, x2, x3)
    max_x = max(x1, x2, x3)
    min_y = min(y1, y2, y3)
    max_y = max(y1, y2, y3)
    if min_x != max_x and max_x > 0 and min_x < 1000000:
        if min_x < 0:
            x_list[0] += 1
        else:
            x_list[min_x + 1] += 1
        if max_x > 1000000:
            x_list[1000000] -= 1
        else:
            x_list[max_x] -= 1
    if min_y != max_y and max_y > 0 and min_y < 1000000:
        if min_y < 0:
            y_list[0] += 1
        else:
            y_list[min_y + 1] += 1
        if max_y > 1000000:
            y_list[1000000] -= 1
        else:
            y_list[max_y] -= 1

for idx in range(1000000):
    x_list[idx + 1] += x_list[idx]
    y_list[idx + 1] += y_list[idx]
    
m = int(input())
for _ in range(m):
    sim, _, num = input().split()
    num = int(num)
    if sim == 'y':
        print(y_list[num])
    else:
        print(x_list[num])