from collections import deque

r, c = map(int, input().split())
matrix = []
for _ in range(r):
    line = list(input())
    matrix.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

answer = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] == "L":
            stack = deque()
            stack.append([i, j])
            answer += 1
            matrix[i][j] = 0
            while stack:
                now_i, now_j = stack.popleft()
                for idx in range(4):
                    ni = now_i + di[idx]
                    nj = now_j + dj[idx]
                    if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] in ["C", "L"]:
                        stack.append([ni, nj])
                        matrix[ni][nj] = 0

print(answer)