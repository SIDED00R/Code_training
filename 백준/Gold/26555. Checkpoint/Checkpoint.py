from collections import deque
import copy
from pickle import FALSE

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n = int(input())
for _ in range(n):
    r, c, d = map(int, input().split())
    matrix = []
    for i in range(r):
        now = []
        line = input()
        for idx in range(c):
            if line[idx] == "S":
                start = [i, idx]
            if line[idx].isnumeric():
                now.append(int(line[idx]))
            elif line[idx] == "E":
                now.append(d + 1)
            else:
                now.append(line[idx])
        matrix.append(now)

    answer = 0
    stack = deque()
    stack.append(start + [0])
    visited_matrix = [[0 for _ in range(c)] for _ in range(r)]
    visited = copy.deepcopy(visited_matrix)
    now_num = 1
    while stack:
        now_i, now_j, w = stack.popleft()
        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] != "#" and visited[ni][nj] == 0:
                if matrix[ni][nj] == now_num:
                    now_num += 1
                    answer += w + 1
                    visited = copy.deepcopy(visited_matrix)
                    if now_num > d + 1:
                        stack = deque()
                    else:
                        stack = deque([[ni, nj, 0]])
                    break
                visited[ni][nj] =  1
                stack.append([ni, nj, w + 1])

    print(answer)