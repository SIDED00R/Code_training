import sys
input = sys.stdin.readline
from collections import deque

def moving(matrix, start, N, M):
    stack = deque([start])
    di = [0 ,0 ,1, -1]
    dj = [1, -1, 0, 0]
    matrix[start[0]][start[1]] = 1
    
    while stack:
        now_i, now_j = stack.popleft()
        for idx in range(4):
            next_i, next_j = now_i + di[idx], now_j + dj[idx]
            if 0 <= next_i < N and 0 <= next_j < M and matrix[next_i][next_j] == 0:
                matrix[next_i][next_j] = matrix[now_i][now_j] + 1
                stack.append([next_i, next_j])

    
N, M = map(int, input().rstrip('\n').split())
start_to_end_map = []
end_to_start_map = []
wall_location = []
for i in range(N):
    line = list(map(int, list(input().rstrip('\n'))))
    for j in range(M):
        if line[j] == 1:
            line[j] = -1
            wall_location.append([i, j])
    start_to_end_map.append(line[:])
    end_to_start_map.append(line[:])
    
moving(start_to_end_map, [0, 0], N, M)
moving(end_to_start_map, [N - 1, M - 1], N, M)

answer = 1e9 if start_to_end_map[-1][-1] == 0 else start_to_end_map[-1][-1]

for wall in wall_location:
    wall_i, wall_j = wall
    di = [0 ,0 ,1, -1]
    dj = [1, -1, 0, 0]
    min_start_to_end = 1e9
    min_end_to_start = 1e9
    for idx in range(4):
        wall_next_i, wall_next_j = wall_i + di[idx], wall_j + dj[idx]
        if 0<= wall_next_i < N and 0 <= wall_next_j < M and start_to_end_map[wall_next_i][wall_next_j] > 0:
            min_start_to_end = min(min_start_to_end, start_to_end_map[wall_next_i][wall_next_j])
        if 0<= wall_next_i < N and 0 <= wall_next_j < M and end_to_start_map[wall_next_i][wall_next_j] > 0:
            min_end_to_start = min(min_end_to_start, end_to_start_map[wall_next_i][wall_next_j])
    answer = min(answer, min_end_to_start + min_start_to_end + 1)


if answer != 1e9:
    print(answer)
else:
    print(-1)
            