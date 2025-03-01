xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
answer = abs(xs - xe) + abs(ys - ye)

tp = [0, first, second, third]


for i in range(4):
    for j in range(4):
        for k in range(4):
            now_x = xs
            now_y = ys
            now_move_count = 0
            if (i == j and i != 0) or (j == k and j != 0) or (k == i and k != 0):
                continue
            else:
                for now in [i, j, k]:
                    if now == 0:
                        continue
                    x1, y1, x2, y2 = tp[now]
                    if abs(now_x - x1) + abs(now_y - y1) > abs(now_x - x2) + abs(now_y - y2):
                        now_move_count += abs(now_x - x2) + abs(now_y - y2) + 10
                        now_x = x1
                        now_y = y1
                    else:
                        now_move_count += abs(now_x - x1) + abs(now_y - y1) + 10
                        now_x = x2
                        now_y = y2
            now_move_count += abs(now_x - xe) + abs(now_y - ye)
            answer = min(answer, now_move_count)
print(answer)