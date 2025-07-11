from collections import defaultdict

xs, ys = map(int, input().split())
t = int(input())
xh, yh = map(int, input().split())
xh -= xs
yh -= ys
n = int(input())

obstacle = set()
for _ in range(n):
    xi, yi = map(int, input().split())
    obstacle.add((xi - xs, yi - ys))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

able_list = defaultdict(int)
able_list[(0, 0)] = 1
answer = 0
for time in range(1, t + 1):
    next_list = defaultdict(int)
    for k, w in able_list.items():
        x, y = k
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if (nx, ny) in obstacle:
                continue
            if (nx, ny) == (xh, yh):
                answer += w
                answer %= 1000000007
                continue
            if abs(nx - xh) + abs(ny - yh) > t - time:
                continue
            next_list[(nx, ny)] += w
            next_list[(nx, ny)] %= 1000000007

    able_list = next_list

print(answer)
                    
        