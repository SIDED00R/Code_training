from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

answer = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue

        h = matrix[i][j]
        visited[i][j] = 1

        comp = [(i, j)]
        q = deque([(i, j)])

        is_peak = True

        while q:
            ci, cj = q.popleft()
            for k in range(8):
                ni, nj = ci + di[k], cj + dj[k]
                if not (0 <= ni < n and 0 <= nj < m):
                    continue

                nh = matrix[ni][nj]

                if nh > h:
                    is_peak = False

                if not visited[ni][nj] and nh == h:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    comp.append((ni, nj))

        if is_peak:
            answer += 1

print(answer)
