from collections import deque

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input()))))
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            stack = deque([[i, j, 0]])
            matrix[i][j] = 1
            
find = False
answer = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
while stack:
    if find:
        break
    now_i, now_j, weight = stack.popleft()
    for idx in range(4):
        ni = now_i + di[idx]
        nj = now_j + dj[idx]
        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != 1:
            if matrix[ni][nj] in [3, 4, 5]:
                find = True
                answer = weight
                break
            matrix[ni][nj] = 1
            stack.append([ni, nj, weight + 1])
            
if find:
    print("TAK")
    print(answer + 1)
else:
    print("NIE")
            
            
