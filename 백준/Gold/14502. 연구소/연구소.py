import sys
input = sys.stdin.readline
from itertools import combinations
import copy

def check(matrix, stack, N, M):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    while stack:
        now_i, now_j = stack.pop()
        for idx in range(4):
            next_i = now_i + di[idx]
            next_j = now_j + dj[idx]
            if 0 <= next_i < N and 0 <= next_j < M and matrix[next_i][next_j] == 0:
                matrix[next_i][next_j] = 2
                stack.append((next_i, next_j))
                

N, M = map(int, input().split())
lab_map = []
for _ in range(N):
    line = list(map(int, input().split()))
    lab_map.append(line)
    
able_space = []
poison = []
for i in range(N):
    for j in range(M):
        if lab_map[i][j] == 0:
            able_space.append(i * M + j)
        elif lab_map[i][j] == 2:
            poison.append((i, j))
         
answer = 0
for case in combinations(able_space, 3):
    count = 0
    new_lab_map = copy.deepcopy(lab_map)
    new_poison = poison[:]
    for num in case:
        new_lab_map[num // M][num % M] = 1
    check(new_lab_map, new_poison, N, M)
    for i in range(N):
        for j in range(M):
            if new_lab_map[i][j] == 0:
                count += 1
    if answer < count:
        answer = count
        
print(answer)

