R, C, K = map(int, input().split())
road = []
for _ in range(R):
    road.append(list(input()))
    
answer = 0
def move(i, j, count):
    global K, R, C, answer
    if count == K:
        if i == 0 and j == C - 1:
            answer += 1
        return
    
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for idx in range(4):
        next_i = i + di[idx]
        next_j = j + dj[idx]
        if 0 <= next_i < R and 0 <= next_j < C and road[next_i][next_j] != "T":
            road[next_i][next_j] = "T"
            move(next_i, next_j, count + 1)
            road[next_i][next_j] = "."
   
road[R - 1][0] = "T"
move(R - 1, 0, 1)
print(answer)
    
