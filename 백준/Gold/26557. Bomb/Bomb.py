from collections import deque

n = int(input())
for _ in range(n):
    answer = 0
    f, r, c = map(int, input().split())
    matrix = []
    dp = [[[1e9 for _ in range(c)] for _ in range(r)] for _ in range(f)]
    for _ in range(f):
        now_floor = []
        for _ in range(r):
            now_floor.append(list(input()))
        matrix.append(now_floor)
    for i in range(f):
        for j in range(r):
            for k in range(c):
                if matrix[i][j][k] == "S":
                    start = [i, j, k]
                    matrix[i][j][k] = "."
    di = [1, -1, 0, 0, 0, 0]
    dj = [0, 0, 1, -1, 0, 0]
    dk = [0, 0, 0, 0, 1, -1]
    stack = deque([start])
    next_stack = []
    find = False
    while True:
        i, j, k = stack.popleft()
        for idx in range(6):
            ni = i + di[idx]
            nj = j + dj[idx]
            nk = k + dk[idx]
            if 0 <= ni < f and 0 <= nj < r and 0 <= nk < c and dp[ni][nj][nk] > answer:
                if matrix[ni][nj][nk] == ".":
                    stack.append([ni, nj, nk])
                    dp[ni][nj][nk] = answer
                elif matrix[ni][nj][nk] == "#":
                    if dp[ni][nj][nk] > answer + 1:
                        next_stack.append([ni, nj, nk])
                        dp[ni][nj][nk] = answer + 1
                else:
                    print(answer)
                    find = True
                    break
            if find:
                break
        if find:
            break
        if stack == deque([]):
            stack = deque(next_stack)
            answer += 1
    
