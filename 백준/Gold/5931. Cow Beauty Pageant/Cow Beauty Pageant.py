from collections import deque
n, m = map(int, input().split())
matrix = []
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for _ in range(n):
    line = list(input())
    matrix.append(line)
    
stack = deque([])
cow_stack = []
find = False
for i in range(n):
    if find:
        break
    for j in range(m):
        if matrix[i][j] == "X":
            find = True
            cow_stack.append([i, j])
            stack.append([i, j, 0])
            matrix[i][j] = 1
            while cow_stack:
                i, j = cow_stack.pop()
                for idx in range(4):
                    ni = di[idx] + i
                    nj = dj[idx] + j
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == "X":
                        matrix[ni][nj] = 1
                        cow_stack.append([ni, nj])
                        stack.append([ni, nj, 0])
                        
            break
     

while stack:
    i, j, w = stack.popleft()
    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < n and 0 <= nj < m:
            if matrix[ni][nj] == ".":
                matrix[ni][nj] = matrix[i][j]
                stack.append([ni, nj, w + 1])
            elif matrix[ni][nj] == "X":
                print(w)
                exit()
    
            