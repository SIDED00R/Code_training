from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

# 방향 설정: L, R, U, D
dirct = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}
directions = ["L", "R", "U", "D"]
visited_matrix = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]
stack = deque()

# A 위치를 찾고 초기 상태 설정
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "A":
            for d, direction in enumerate(directions):
                stack.append((i, j, 0, d))  # (i, j, weight, direction index)
                visited_matrix[i][j][d] = True

# BFS 수행
while stack:
    now_i, now_j, weight, direction_idx = stack.popleft()
    direction = directions[direction_idx]
    di, dj = dirct[direction]

    # 현재 방향으로 계속 직진
    next_i, next_j = now_i + di, now_j + dj
    while 0 <= next_i < n and 0 <= next_j < n and matrix[next_i][next_j] != 'x':
        if matrix[next_i][next_j] == 'B':
            print(weight)
            exit()
        
        # 현재 방향으로 방문하지 않은 경우에만 처리
        if not visited_matrix[next_i][next_j][direction_idx]:
            visited_matrix[next_i][next_j][direction_idx] = True
            # 현재 방향 유지하며 큐에 추가
            stack.append((next_i, next_j, weight, direction_idx))
            # 다른 두 방향으로 회전하며 큐에 추가
            for new_direction_idx in range(4):
                if new_direction_idx != direction_idx:
                    stack.append((next_i, next_j, weight + 1, new_direction_idx))
                    visited_matrix[next_i][next_j][new_direction_idx] = True
        
        # 다음 칸으로 이동
        next_i += di
        next_j += dj
