n = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for _ in range(n):
    answer = 0
    w, h = map(int, input().split())
    matrix = []
    for _ in range(h):
        matrix.append(list(input()))
    fire = []
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "*":
                fire.append([i, j])
            elif matrix[i][j] == "@":
                now = [[i, j]]
    find = False
    while True:
        answer += 1
        next_now = []
        next_fire = []
        while now:
            i, j = now.pop()
            if matrix[i][j] != "@":
                continue
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if 0 <= ni < h and 0 <= nj < w:
                    if matrix[ni][nj] == ".":
                        matrix[ni][nj] = "@"
                        next_now.append([ni, nj])
                else:
                    find = True
                    break
        while fire:
            i, j = fire.pop()
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if 0 <= ni < h and 0 <= nj < w and matrix[ni][nj] != "#" and matrix[ni][nj] != "*":
                    matrix[ni][nj] = "*"
                    next_fire.append([ni, nj])
        now = next_now[:]
        fire = next_fire[:]
        if find or now == []:
            break
    if find:
        print(answer)
    else:
        print("IMPOSSIBLE")