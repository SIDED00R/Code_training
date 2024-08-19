def move(direction, i, j):
    if visited[i][j]:
        return 0
    count = 0
    d = {0:[-1, 0], 1:[0, 1], 2: [1, 0], 3: [0, -1]}
    while 0 <= i < n and 0 <= j < m:
        count += 1
        now = matrix[i][j]
        if now == "/":
            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 3
            elif direction == 3:
                direction = 2
        else:
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 0
        di, dj = d[direction]
        i += di
        j += dj
    visited[i - di][j - dj] = True
    return count
        
answer = 0
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
    
visited = [[False for _ in range(m)] for _ in range(n)]
    
for i in range(n):
    for j in range(m):
        if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and not visited[i][j]:
            if i == 0:
                answer = max(answer, move(2, i, j))
            if i == n - 1:
                answer = max(answer, move(0, i, j))
            if j == 0:
                answer = max(answer, move(1, i, j))
            if j == m - 1:
                answer = max(answer, move(3, i, j))
            visited[i][j] == True
            
print(answer)
            
            