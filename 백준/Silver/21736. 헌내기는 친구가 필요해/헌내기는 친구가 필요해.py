import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    line = input()
    for j in range(M):
        if line[j] == "I":
            stack = [[i, j]]
            visited[i][j] = True
        elif line[j] == "X":
            visited[i][j] = True
        board[i][j] = line[j]
        
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
new_stack = []
answer = 0
while stack:
    now_i, now_j = stack.pop()
    if board[now_i][now_j] == "P":
        answer += 1
    for idx in range(4):
        if now_i + di[idx] >= 0 and now_i + di[idx] < N and now_j + dj[idx] >= 0 and now_j + dj[idx] < M:
            if not visited[now_i + di[idx]][now_j + dj[idx]]:
                visited[now_i + di[idx]][now_j + dj[idx]] = True
                new_stack.append([now_i + di[idx], now_j + dj[idx]])

    if not stack:
        stack = new_stack[:]
        new_stack = []

if answer == 0:
    print("TT")
else:
    print(answer)

        