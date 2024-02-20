import sys
input = sys.stdin.readline

R, C, T = map(int, input().rstrip('\n').split())

room_map = [[0 for _ in range(C)] for _ in range(R)]
air = []
for i in range(R):
    line  = list(map(int, input().rstrip('\n').split()))
    for j in range(C):
        if line[j] == -1:
            air.append([i, j])
        room_map[i][j] = [line[j], 0]
    
air_up = air[0]
air_down = air[1]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for _ in range(T):
    for i in range(R):
        for j in range(C):
            num = room_map[i][j][0]
            if num > 0:
                move = num // 5
                for idx in range(4):
                    next_i = i + di[idx]
                    next_j = j + dj[idx]
                    if 0 <= next_i < R and 0 <= next_j < C and room_map[next_i][next_j][0] != -1:
                        room_map[next_i][next_j][1] += move
                        room_map[i][j][0] -= move
    for ii in range(R):
        for jj in range(C):
            room_map[ii][jj] = [sum(room_map[ii][jj]), 0]
        
    air_up_i, air_up_j = air_up
    keep = 0
    air_up_j += 1
    while air_up_j != C:
        keep, room_map[air_up_i][air_up_j][0] = room_map[air_up_i][air_up_j][0], keep
        air_up_j += 1
    air_up_j -= 1
    air_up_i -= 1
    while air_up_i != 0:
        keep, room_map[air_up_i][air_up_j][0] = room_map[air_up_i][air_up_j][0], keep
        air_up_i -= 1
    while air_up_j != 0:
        keep, room_map[air_up_i][air_up_j][0] = room_map[air_up_i][air_up_j][0], keep
        air_up_j -= 1
    while air_up_i != air_up[0]:
        keep, room_map[air_up_i][air_up_j][0] = room_map[air_up_i][air_up_j][0], keep
        air_up_i += 1
        
    air_down_i, air_down_j = air_down
    keep = 0
    air_down_j += 1
    while air_down_j != C:
        keep, room_map[air_down_i][air_down_j][0] = room_map[air_down_i][air_down_j][0], keep
        air_down_j += 1
    air_down_j -= 1
    air_down_i += 1
    while air_down_i != R:
        keep, room_map[air_down_i][air_down_j][0] = room_map[air_down_i][air_down_j][0], keep
        air_down_i += 1
    air_down_i -= 1
    air_down_j -= 1
    while air_down_j != 0:
        keep, room_map[air_down_i][air_down_j][0] = room_map[air_down_i][air_down_j][0], keep
        air_down_j -= 1
    while air_down_i != air_down[0]:
        keep, room_map[air_down_i][air_down_j][0] = room_map[air_down_i][air_down_j][0], keep
        air_down_i -= 1
    
answer = 0
for i in range(R):
    for j in range(C):
        answer += room_map[i][j][0]

print(answer + 2)
        