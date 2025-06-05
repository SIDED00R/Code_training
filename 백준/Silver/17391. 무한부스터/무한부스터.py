from collections import deque

n, m = map(int, input().split())
matrix = []
visited = [[-1 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

stack = deque([[0, 0, 0]])
visited[0][0] = 0
while stack:
    now_i, now_j, weight = stack.popleft()
    power = matrix[now_i][now_j]
    for idx in range(power):
        if now_i + idx  + 1 < n and visited[now_i + idx + 1][now_j] == -1:
            visited[now_i + idx + 1][now_j] = weight + 1
            stack.append([now_i + idx + 1, now_j, weight + 1])
        if now_j + idx + 1 < m and visited[now_i][now_j + idx + 1] == -1:
            visited[now_i][now_j + idx + 1] = weight + 1
            stack.append([now_i, now_j + idx + 1, weight + 1])
    if visited[-1][-1] != -1:
        print(visited[-1][-1])
        break