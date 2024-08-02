from collections import deque

# Input matrix and start position
matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))
r, c = map(int, input().split())

# Direction vectors for movement
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# BFS initialization
queue = deque([[r, c, 0]])
answer = 0
find_number = 1

# Visited matrix
visited_matrix = [[False for _ in range(5)] for _ in range(5)]
visited_matrix[r][c] = True

# BFS loop
while queue:
    if find_number == 7:
        break
    i, j, count = queue.popleft()
    for idx in range(4):
        next_i, next_j = i + di[idx], j + dj[idx]
        if 0 <= next_i < 5 and 0 <= next_j < 5 and matrix[next_i][next_j] != -1 and not visited_matrix[next_i][next_j]:
            visited_matrix[next_i][next_j] = True
            if matrix[next_i][next_j] == find_number:
                answer += count + 1
                queue = deque([[next_i, next_j, 0]])
                find_number += 1
                visited_matrix = [[False for _ in range(5)] for _ in range(5)]
                visited_matrix[next_i][next_j] = True
                break
            else:
                queue.append([next_i, next_j, count + 1])
        # Inner while loop to extend search in the current direction
        now_i, now_j = i, j
        while 0 <= next_i < 5 and 0 <= next_j < 5 and matrix[next_i][next_j] != -1:
            now_i, now_j = next_i, next_j
            next_i, next_j = now_i + di[idx], now_j + dj[idx]
            if matrix[now_i][now_j] == 7:
                break
        if matrix[now_i][now_j] == find_number:
            answer += count + 1
            queue = deque([[now_i, now_j, 0]])
            find_number += 1
            visited_matrix = [[False for _ in range(5)] for _ in range(5)]
            visited_matrix[now_i][now_j] = True
            break
        elif not visited_matrix[now_i][now_j]:
            visited_matrix[now_i][now_j] = True
            queue.append([now_i, now_j, count + 1])

# Output result
if find_number == 7:
    print(answer)
else:
    print(-1)
