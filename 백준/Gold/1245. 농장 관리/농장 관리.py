n, m = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

visited = [[0 for _ in range(m)] for _ in range(n)]

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
answer = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            continue
        visited[i][j] = 1
        stack = [[i, j]]
        able_stack = [[i, j]]
        
        height = matrix[i][j]
        if height == 0:
            visited[i][j] = 1
            continue

        while stack:
            now_i, now_j = stack.pop()
            for idx in range(8):
                ni = now_i + di[idx]
                nj = now_j + dj[idx]
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] != 1 and matrix[ni][nj] == height:
                    visited[ni][nj] = 1
                    able_stack.append([ni, nj])
                    stack.append([ni, nj])

        top = True
        for now_node in able_stack:
            now_i, now_j = now_node
            for idx in range(8):
                ni = now_i + di[idx]
                nj = now_j + dj[idx]
                if 0 <= ni < n and 0 <= nj < m:
                    if height < matrix[ni][nj]:
                        top = False
                        break
            if not top:
                break
        if top:
            answer += 1

print(answer)

            