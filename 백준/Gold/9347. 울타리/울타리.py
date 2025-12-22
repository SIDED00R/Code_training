import sys
from collections import deque

input = sys.stdin.readline
INF = 10**18

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(r)]

    dist = [[INF] * c for _ in range(r)]
    dq = deque()

    def try_start(i, j):
        cost = matrix[i][j]
        if dist[i][j] > cost:
            dist[i][j] = cost
            if cost == 0:
                dq.appendleft((i, j))
            else:
                dq.append((i, j))

    for i in range(r):
        try_start(i, 0)
        try_start(i, c - 1)
    for j in range(c):
        try_start(0, j)
        try_start(r - 1, j)

    di = (0, 0, 1, -1)
    dj = (1, -1, 0, 0)

    while dq:
        x, y = dq.popleft()
        cur = dist[x][y]

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < r and 0 <= ny < c:
                w = matrix[nx][ny]
                nd = cur + w
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    if w == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

    max_break = -1
    flower_cnt = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                d = dist[i][j]
                if d > max_break:
                    max_break = d
                    flower_cnt = 1
                elif d == max_break:
                    flower_cnt += 1

    print(max_break, flower_cnt)
