from collections import deque

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

check_matrix = [[[-1] * (1 << 6) for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "0":
            start = (i, j, 0)
            check_matrix[i][j][0] = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

positions = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

queue = deque([start])

while queue:
    i, j, state = queue.popleft()
    count = check_matrix[i][j][state]
    
    for idx in range(4):
        ni, nj = i + di[idx], j + dj[idx]
        
        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != "#":
            new_state = state
            
            if 'A' <= matrix[ni][nj] <= 'F':
                if state & (1 << positions[matrix[ni][nj]]) == 0:
                    continue
            
            elif 'a' <= matrix[ni][nj] <= 'f':
                new_state |= (1 << positions[matrix[ni][nj].upper()])
            
            if matrix[ni][nj] == "1":
                print(count + 1)
                exit()
            
            if check_matrix[ni][nj][new_state] == -1 or check_matrix[ni][nj][new_state] > count + 1:
                check_matrix[ni][nj][new_state] = count + 1
                queue.append((ni, nj, new_state))

print(-1)
