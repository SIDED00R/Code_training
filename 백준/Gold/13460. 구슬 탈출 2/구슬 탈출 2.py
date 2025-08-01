def move(rx, ry, bx, by, dx, dy):
    find = 0
    move_r = 0
    move_b = 0
    while True:
        move_r += 1
        rx += dx
        ry += dy
        if matrix[rx][ry] == '#':
            rx -= dx
            ry -= dy
            break
        elif [rx, ry] == end:
            find = 1
            break

    while True:
        move_b += 1
        bx += dx
        by += dy
        if matrix[bx][by] == '#':
            bx -= dx
            by -= dy
            break
        elif [bx, by] == end:
            find = 2
            break

    if [rx, ry] == [bx, by]:
        if move_r > move_b:
            rx -= dx
            ry -= dy
        else:
            bx -= dx
            by -= dy

    return (rx, ry, bx, by), find

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)
stack = [[0, 0, 0, 0]]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            stack[0][0] = i
            stack[0][1] = j
            matrix[i][j] = '.'
        elif matrix[i][j] == 'B':
            stack[0][2] = i
            stack[0][3] = j
            matrix[i][j] = '.'
        elif matrix[i][j] == 'O':
            end = [i, j]
          
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for idx in range(1, 11):
    s = set()
    for now_stack in stack:
        rx, ry, bx, by = now_stack
        for d in range(4):
            next_case, able = move(rx, ry, bx, by, di[d], dj[d])
            if able == 1:
                print(idx)
                exit()
            elif able == 2:
                continue
            else:
                s.add(next_case)

    stack = list(s)

print(-1)
        