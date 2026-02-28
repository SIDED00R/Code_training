from collections import deque

v, m = map(int, input().split())
xs, xy = map(float, input().split())
xt, yt = map(float, input().split())
bunker = []
while True:
    try:
        x, y = map(float, input().split())
        bunker.append([x, y])
    except:
        break

able = deque([[xs, xy, 0]])
visited = [False for _ in range(len(bunker))]
while able:
    x, y, w = able.popleft()
    if (xt - x) ** 2 + (yt - y) ** 2 <= (v * 60 * m) ** 2:
        print(f"Yes, visiting {w} other holes.")
        exit()
    for idx in range(len(bunker)):
        if not visited[idx]:
            nx, ny = bunker[idx]
            if (nx - x) ** 2 + (ny - y) ** 2 <= (v * 60 * m) ** 2:
                visited[idx] = True
                able.append([nx, ny, w + 1])
            
print("No.")