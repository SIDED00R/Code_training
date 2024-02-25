import sys
input = sys.stdin.readline
import copy

N, M = map(int, input().rstrip('\n').split())
chess_map = []
for i in range(N):
    line = list(map(int, input().rstrip('\n').split()))
    chess_map.append(line)
    
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
air_count = 1
able_chess = []
for i in range(N):
    for j in range(M):
        if chess_map[i][j] == 0:
            air_count += 1
            stack = [[i, j]]
            chess_map[i][j] = air_count
            while stack:
                now_i, now_j = stack.pop()
                for idx in range(4):
                    next_i, next_j = now_i + di[idx], now_j + dj[idx]
                    if 0 <= next_i < N and 0 <= next_j < M and chess_map[next_i][next_j] == 0:
                        chess_map[next_i][next_j] = air_count
                        stack.append([next_i, next_j])
                        
        elif chess_map[i][j] == 1:
            able_chess.append([i, j])
                       
now_dirty_air = set([2])
next_dirty_air = now_dirty_air.copy()
next_chess_map = copy.deepcopy(chess_map)
answer = 0
while able_chess:
    answer += 1
    next_able_chess = []
    for chess in able_chess:
        chess_i, chess_j = chess
        count = 0
        for idx in range(4):
            next_chess_i, next_chess_j = chess_i + di[idx], chess_j + dj[idx]
            if 0 <= next_chess_i < N and 0 <= next_chess_j < M and chess_map[next_chess_i][next_chess_j] in now_dirty_air:
                count += 1
        if count < 2:
            next_able_chess.append(chess)
        else:
            next_chess_map[chess_i][chess_j] = 2
            for idx in range(4):
                next_chess_i, next_chess_j = chess_i + di[idx], chess_j + dj[idx]
                if 0 <= next_chess_i < N and 0 <= next_chess_j < M and chess_map[next_chess_i][next_chess_j] != 1 and chess_map[next_chess_i][next_chess_j] not in now_dirty_air:
                    next_dirty_air.add(chess_map[next_chess_i][next_chess_j])
    able_chess = next_able_chess[:]
    now_dirty_air = next_dirty_air.copy()
    chess_map = copy.deepcopy(next_chess_map)
    
print(answer)
