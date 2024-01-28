import sys
input = sys.stdin.readline

M, N, H = map(int, input().rstrip('\n').split())
tomato = [[] for _ in range(H)]
for k in range(H):
    for _ in range(N):
        line = list(map(int, input().rstrip('\n').split()))
        tomato[k].append(line)
 
di = [0, 0, 0, 0, 1, -1]
dj = [0, 0, 1, -1, 0, 0]
dk = [1, -1, 0, 0, 0, 0]

stack = []
left_tomato = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1:
                stack.append((k, i, j))
            elif tomato[k][i][j] == 0:
                left_tomato += 1
                
if left_tomato == 0:
    print(0)
else:
    count = 0
    new_stack = []
    while stack:
        now_k, now_i, now_j = stack.pop()
        for idx in range(6):
            next_k, next_i, next_j = now_k + dk[idx], now_i + di[idx], now_j + dj[idx]
            if 0 <= next_k < H and 0 <= next_i < N and 0 <= next_j < M and tomato[next_k][next_i][next_j] == 0:
                tomato[next_k][next_i][next_j] = 1
                new_stack.append((next_k, next_i, next_j))
                left_tomato -= 1
        if not stack:
            stack = new_stack[:]
            new_stack = []
            count += 1
            if left_tomato == 0:
                print(count)
                break       
if left_tomato:
    print(-1)
        
        