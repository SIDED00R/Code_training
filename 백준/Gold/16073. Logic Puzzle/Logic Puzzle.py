n, m = map(int, input().split())

matrix = []
for _ in range(n + 2):
    line = list(map(int, input().split()))
    matrix.append(line)

block = [1 for _ in range(m + 2)]
check_matrix = []
check_matrix.append(block)
for _ in range(n):
    check_matrix.append([1] + [0 for _ in range(m)] + [1])
check_matrix.append(block)

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
d = {0:[0, 1], 1:[1, 0], 2:[0, -1], 3:[-1, 0]}
direction = 0

visit_matrix = [[0 for _ in range(m + 2)] for _ in range(n + 2)]

for count in range((min(n, m) + 1) // 2 + 1):
    bi1 = 0 + count
    bi2 = n + 2 - count
    bj1 = 0 + count
    bj2 = m + 2 - count
    
    now_i, now_j = bi1, bj1
    visit_matrix[now_i][now_j] = 1

    while True:
        count = 0
        find_i, find_j = -1, -1
        find = False
        if check_matrix[now_i][now_j] == 2:
            count += 1
        for idx in range(8):
            ci = now_i + di[idx]
            cj = now_j + dj[idx]
            if 0 <= ci < n + 2 and 0 <= cj < m + 2:
                if check_matrix[ci][cj] == 2:
                    count += 1
                elif check_matrix[ci][cj] == 0:
                    find = True
                    find_i, find_j = ci, cj

        now_count = matrix[now_i][now_j]
        if count == now_count:
            if find:
                check_matrix[find_i][find_j] = 1
        elif now_count == count + 1 and find:
            check_matrix[find_i][find_j] = 2
        else:
            print("impossible")
            exit()

        next_i = now_i + d[direction][0]
        next_j = now_j + d[direction][1]
        if not (bi1 <= next_i < bi2 and bj1 <= next_j < bj2):
            direction = (direction + 1) % 4
            next_i = now_i + d[direction][0]
            next_j = now_j + d[direction][1]

        now_i, now_j = next_i, next_j
        if visit_matrix[now_i][now_j] == 1:
            break
        else:
            visit_matrix[now_i][now_j] = 1


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if check_matrix[i][j] == 1:
            print(".", end = "")
        else:
            print("X", end = "")
    print()

