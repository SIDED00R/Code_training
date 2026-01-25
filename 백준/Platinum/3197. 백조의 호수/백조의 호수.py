from collections import deque

matrix = []
start = []
stack = deque()
r, c = map(int, input().split())
for i in range(r):
    line = list(input())
    for j in range(c):
        if line[j] == "L":
            start.append([i, j])
            stack.append([i, j])
            line[j] = 0
        if line[j] == ".":
            stack.append([i, j])
            line[j] = 0
    matrix.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while stack:
    i, j = stack.popleft()
    weight = matrix[i][j]
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] == "X":
            matrix[ni][nj] = weight + 1
            stack.append([ni, nj])

si, sj = start[0]
gi, gj = start[1]
visited = [[False for _ in range(c)] for _ in range(r)]
visited[si][sj] = True
stack = [[si, sj]]
count = 0
next_stack = []
while stack:
    if visited[gi][gj]:
        print(count)
        break
    i, j = stack.pop()
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < r and 0 <= nj < c and visited[ni][nj] == False:
            if matrix[ni][nj] <= count:
                visited[ni][nj] = True
                stack.append([ni, nj])
            else:
                next_stack.append([i, j])
    if not stack:
        stack = next_stack[:]
        next_stack = []
        count += 1