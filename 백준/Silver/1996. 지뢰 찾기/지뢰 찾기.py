N = int(input())
mine_map = []
for _ in range(N):
    mine_map.append(list(input()))
    
answer_map = [["*" for _ in range(N)] for _ in range(N)]

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

for i in range(N):
    for j in range(N):
        if mine_map[i][j] == ".":
            total = 0
            for idx in range(8):
                next_i = i + di[idx]
                next_j = j + dj[idx]
                if 0 <= next_i < N and 0 <= next_j < N and mine_map[next_i][next_j] != ".":
                    total += int(mine_map[next_i][next_j])
            answer_map[i][j] = str(total) if total < 10 else "M"          
            
for l in answer_map:
    print("".join(l))
        
                    
        