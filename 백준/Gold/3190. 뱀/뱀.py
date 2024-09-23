from collections import deque

n = int(input())
k = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    row, col = map(int, input().split())
    matrix[row - 1][col - 1] = 1

l = int(input())
snake = deque([[0, 0]])

now_d = "R"
d = {"U":[-1, 0], "R":[0, 1], "D":[1, 0], "L":[0, -1]}
change_L = {"U": "L","R": "U","L": "D","D": "R"}
change_D = {"U": "R","R": "D","L": "U","D": "L"}
now_time = 0
for _ in range(l):
    time, move = input().split()
    time = int(time)
    di, dj= d[now_d]
    for t in range(time - now_time):
        head_i, head_j = snake[0]
        ni = head_i + di
        nj = head_j + dj
        if 0 <= ni < n and 0 <= nj < n:
            if [ni, nj] in snake:
                print(now_time + t + 1)
                exit()
            else:
                snake.appendleft([ni, nj])
                if matrix[ni][nj] != 1:
                    snake.pop()
                else:
                    matrix[ni][nj] = 0
        else:
            print(now_time + t + 1)
            exit()
    now_time = time
    if move == "L":
        now_d = change_L[now_d]
    else:
        now_d = change_D[now_d]

di, dj= d[now_d]
while True:
    now_time += 1
    head_i, head_j = snake[0]
    ni = head_i + di
    nj = head_j + dj
    if 0 <= ni < n and 0 <= nj < n:
        if [ni, nj] in snake:
            print(now_time)
            exit()
        else:
            snake.appendleft([ni, nj])
            if matrix[ni][nj] != 1:
                snake.pop()
    else:
        print(now_time)
        exit()