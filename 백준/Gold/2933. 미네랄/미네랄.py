import copy

def shoot(num, turn, c):
    find = False
    if turn == 0:
        for j in range(c):
            if matrix[num][j] == "x":
                matrix[num][j] = "."
                find = True
                break
    else:
        for j in range(c):
            if matrix[num][c - j - 1] == "x":
                find = True
                matrix[num][c - j - 1] = "."
                break
    return find

def fall(r, c):
    copy_matrix = copy.deepcopy(matrix)
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    stack = []
    for i in range(r):
        for j in range(c):
            if copy_matrix[i][j] == "x":
                stack.append([i, j])
                copy_matrix[i][j] = "."
                find = True
                now_node = []
                now_node.append([i, j])

                while stack:
                    now_i, now_j = stack.pop()
                    for idx in range(4):
                        ni = now_i + di[idx]
                        nj = now_j + dj[idx]
                        if 0 <= ni < r and 0 <= nj < c and copy_matrix[ni][nj] == "x":
                            copy_matrix[ni][nj] = "."
                            stack.append([ni, nj])
                            now_node.append([ni, nj])
                        if ni == r:
                            find = False
                
                bottom = []
                if find:
                    for now_case in now_node:
                        i, j = now_case
                        if matrix[i + 1][j] == ".":
                            bottom.append([i, j])

                while find:
                    out = False
                    for now_case in bottom:
                        i, j = now_case
                        if i + 1 == r or matrix[i + 1][j] == "x":
                            out = True
                            break
                    if out:
                        break
                    else:
                        for idx in range(len(bottom)):
                            bottom[idx] = [bottom[idx][0] + 1, bottom[idx][1]]

                    for now_case in now_node:
                        i, j = now_case
                        matrix[i][j] = "."
                    for now_case in now_node:
                        i, j = now_case
                        matrix[i + 1][j] = "x"
                    for idx in range(len(now_node)):
                        i, j = now_node[idx]
                        now_node[idx] = [i + 1, j]

                if find:
                    return


r, c = map(int, input().split())
matrix = []
for _ in range(r):
    matrix.append(list(input()))

n = int(input())
throw = list(map(int, input().split()))

turn = 0
for num in throw:
    change = shoot(r - num, turn, c)
    turn = (turn + 1) % 2
    
    if change:
        fall(r, c)

for l in matrix:
    print("".join(l))
