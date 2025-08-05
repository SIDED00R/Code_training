from collections import deque

x, y, n = map(int, input().split())
matrix = [[0 for _ in range(1001)] for _ in range(1001)]
x += 500
y += 500
for _ in range(n):
    a, b = map(int, input().split())
    a += 500
    b += 500
    matrix[a][b] = 1

visited = [[False for _ in range(1001)] for _ in range(1001)]
stack = deque([[500, 500, 0]])
visited[500][500] = True
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
while True:
    now_i, now_j, w = stack.popleft()
    for idx in range(4):
        ni = now_i + di[idx]
        nj = now_j + dj[idx]
        if 0 <= ni < 1001 and 0 <= nj < 1001 and not visited[ni][nj] and matrix[ni][nj] != 1:
            visited[ni][nj] = True
            stack.append([ni, nj, w + 1])
            if [ni, nj] == [x, y]:
                print(w + 1)
                exit()
            