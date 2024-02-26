import sys
input = sys.stdin.readline

N = int(input())
food_map = []
for i in range(N):
    line = list(map(int, input().rstrip('\n').split()))
    for j in range(N):
        if line[j] == 9:
            shark = [i, j]
    food_map.append(line)
 
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
shark_size = 2
answer = 0
eat_count = 0
food_map[shark[0]][shark[1]] = 0

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    stack = [shark]
    next_stack = []
    able_case = []
    move_count = 0
    find = False
    while stack:
        now_i, now_j = stack.pop()
        for idx in range(4):
            next_i, next_j = now_i + di[idx], now_j + dj[idx]
            if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j] and food_map[next_i][next_j] <= shark_size:
                next_stack.append([next_i, next_j])
                visited[next_i][next_j] = True
                if 0 < food_map[next_i][next_j] < shark_size:
                    find = True
                    able_case.append([next_i, next_j])
        if not stack:
            if find:
                able_case = sorted(able_case)
                shark = able_case[0]
                food_map[shark[0]][shark[1]] = 0
                answer += move_count + 1
                eat_count += 1
                if eat_count == shark_size:
                    shark_size += 1
                    eat_count = 0
                break
            else:
                stack = next_stack[:]
                next_stack = []
                move_count += 1
    if not find:
        break
                
print(answer)
    
