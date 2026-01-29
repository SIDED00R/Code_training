n, m, k = map(float, input().split())
n = int(n)
m = int(m)
matrix = []
for _ in range(2 * m + 1):
    line = list(input())
    matrix.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

board = [[0 for _ in range(n)] for _ in range(m)]
count = 0
for i in range(1, 2 * m + 1, 2):
    for j in range(1, 2 * n + 1, 2):
        bi = (i - 1) // 2
        bj = (j - 1) // 2
        if board[bi][bj] == 0:
            if matrix[i][j] == "O":
                board[(i - 1) // 2][(j - 1) // 2] = -1
            else:
                count += 1
                answer_stack = [[i, j]]
                stack = [[i, j]]
                while stack:
                    now_i, now_j = stack.pop()
                    for idx in range(4):
                        ni = now_i + di[idx]
                        nj = now_j + dj[idx]
                        if matrix[ni][nj] == '.':
                            matrix[ni][nj] = "+"
                            answer_stack.append([now_i + di[idx] * 2, now_j + dj[idx] * 2])
                            stack.append([now_i + di[idx] * 2, now_j + dj[idx] * 2])
                for ni, nj in answer_stack:
                    board[(ni - 1) // 2][(nj - 1) // 2] = count

x = k
points = []
dx = -1
for y in range(m, -1, -1):
    points.append([y, x])
    nx = x + dx
    if nx < 0:
        dx = 1
        nx = -nx
    elif nx > n:
        nx = 2 * n - nx
        dx = -1
    x = nx
for y in range(1, m + 1):
    points.append([y, x])
    nx = x + dx
    if nx < 0:
        dx = 1
        nx = -nx
    elif nx > n:
        nx = 2 * n - nx
        dx = -1
    x = nx

answer = set()
if int(k) == int(k - 0.5):
    for idx in range(1, len(points)):
        front = points[idx - 1]
        back = points[idx]
        min_y = min(front[0], back[0])
        answer.add(board[min_y][int(front[1] - 0.5)])
        answer.add(board[min_y][int(back[1] - 0.5)])
else:
    for idx in range(1, len(points)):
        front = points[idx - 1]
        back = points[idx]
        min_y = min(front[0], back[0])
        min_x = int(min(front[1], back[1]))
        answer.add(board[min_y][min_x])

answer.discard(-1)
print(len(answer))