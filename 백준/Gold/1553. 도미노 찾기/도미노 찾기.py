def check(i, j, dic):
    global answer
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < 8 and 0 <= nj < 7 and not visited[ni][nj]:
            min_value = min(matrix[ni][nj], matrix[i][j])
            max_value = max(matrix[ni][nj], matrix[i][j])
            if dic[(min_value, max_value)] == 0:
                dic[(min_value, max_value)] = 1
                visited[ni][nj] = True
                visited[i][j] = True
                find = False
                for next_i in range(8):
                    for next_j in range(7):
                        if not visited[next_i][next_j]:
                            find = True
                            break
                    if find:
                        break
                if find:
                    check(next_i, next_j, dic)
                else:
                    answer += 1
                visited[ni][nj] = False
                visited[i][j] = False
                dic[(min_value, max_value)] = 0

answer = 0
matrix = []
for _ in range(8):
    line = list(map(int, list(input())))
    matrix.append(line)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

dic = {}
for i in range(7):
    for j in range(i, 7):
        dic[(i, j)] = 0

visited = [[False for _ in range(7)] for _ in range(8)]
check(0, 0, dic)
print(answer)