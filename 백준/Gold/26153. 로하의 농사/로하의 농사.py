def find(now_i, now_j, left_weight, total, d, n, m):
    global answer
    for idx in range(4):
        ni = now_i + di[idx]
        nj = now_j + dj[idx]
        if d == -1:
            spend = 1
        elif d == idx:
            spend = 1
        else:
            spend = 2
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and left_weight >= spend:
            visited[ni][nj] = True
            answer = max(answer, total + matrix[ni][nj])
            find(ni, nj, left_weight - spend, total + matrix[ni][nj], idx, n, m)
            visited[ni][nj] = False

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

x, y, p = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
visited[x][y] = True
total = matrix[x][y]
answer = total

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
find(x, y, p, total, -1, n, m)
print(answer)