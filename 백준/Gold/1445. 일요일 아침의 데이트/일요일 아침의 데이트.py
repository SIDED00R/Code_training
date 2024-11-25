from collections import deque

def check(i, j):
     for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < n and 0 <= nj < m:
            if matrix[ni][nj] == "g":
                return True
     return False

n, m = map(int, input().split())
matrix = []
stack = deque([])
for i in range(n):
    line = list(input())
    for j in range(m):
        if line[j] == "S":
            stack.append([i, j])
    matrix.append(line)

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
weight = [[[n * m + 1, n * m  +1] for _ in range(m)] for _ in range(n)]
i, j = stack[0]

answer_1 = m * n + 1
answer_2 = m * n + 1
weight[i][j] = [0, 0]
while stack:
    i, j = stack.popleft()
    if weight[i][j][0] > answer_1:
        continue
    elif weight[i][j][0] == answer_1:
        if weight[i][j][1] > answer_2:
            continue
    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < n and 0 <= nj < m:
            if matrix[ni][nj] == "g":
                if weight[ni][nj][0] > weight[i][j][0] + 1:
                    weight[ni][nj][0] = weight[i][j][0] + 1
                    weight[ni][nj][1] = weight[i][j][1]
                    stack.append([ni, nj])
                elif weight[ni][nj][0] == weight[i][j][0] + 1:
                    if weight[ni][nj][1] > weight[i][j][1]:
                        weight[ni][nj][1] = weight[i][j][1]
                        stack.append([ni, nj])
            elif matrix[ni][nj] == ".":
                if check(ni, nj):
                    near = 1
                else:
                    near = 0
                if weight[ni][nj][0] > weight[i][j][0]:
                    weight[ni][nj][0] = weight[i][j][0]
                    weight[ni][nj][1] = weight[i][j][1] + near
                    stack.append([ni, nj])
                elif weight[ni][nj][0] == weight[i][j][0]:
                    if weight[ni][nj][1] > weight[i][j][1] + near:
                        weight[ni][nj][1] = weight[i][j][1] + near
                        stack.append([ni, nj])
            else:
                if weight[ni][nj][0] > weight[i][j][0]:
                    weight[ni][nj][0] = weight[i][j][0]
                    weight[ni][nj][1] = weight[i][j][1]
                    answer_1 = weight[i][j][0]
                    answer_2 = weight[i][j][1]
                elif weight[ni][nj][0] == weight[i][j][0]:
                    if weight[ni][nj][1] > weight[i][j][1]:
                        weight[ni][nj][1] = weight[i][j][1]
                        answer_2 = weight[i][j][1]

print(answer_1, answer_2)

