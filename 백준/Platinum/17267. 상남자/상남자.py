import copy

def check_ud(n):
    add_stack = []
    for now_case in stack:
        now_i, now_j, now_l, now_r = now_case
        for di in range(1, n):
            next_i = now_i + di
            if 0 <= next_i < n and not visit_matrix[next_i][now_j] and matrix[next_i][now_j] != 1:
                visit_matrix[next_i][now_j] = True
                add_stack.append([next_i, now_j, now_l, now_r])
            else:
                break
        for di in range(1, n):
            next_i = now_i - di
            if 0 <= next_i < n and not visit_matrix[next_i][now_j] and matrix[next_i][now_j] != 1:
                visit_matrix[next_i][now_j] = True
                add_stack.append([next_i, now_j, now_l, now_r])
            else:
                break
    stack.extend(add_stack)


n, m = map(int, input().split())
l, r = map(int, input().split())

matrix = []
visit_matrix = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    line = list(map(int, list(input())))
    matrix.append(line)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            stack = [[i, j, l, r]]
now_i, now_j, now_l, now_r = stack[0]
visit_matrix[now_i][now_j] = True

while stack:
    check_ud(n)
    next_stack = []
    while stack:
        now_i, now_j, now_l, now_r = stack.pop()
        if now_l >= 1:
            next_j = now_j - 1
            if 0 <= next_j < m and not visit_matrix[now_i][next_j] and matrix[now_i][next_j] != 1:
                visit_matrix[now_i][next_j] = True
                next_stack.append([now_i, next_j, now_l - 1, now_r])
        if now_r >= 1:
            next_j = now_j + 1
            if 0 <= next_j < m and not visit_matrix[now_i][next_j] and matrix[now_i][next_j] != 1:
                visit_matrix[now_i][next_j] = True
                next_stack.append([now_i, next_j, now_l, now_r - 1])
    stack = copy.deepcopy(next_stack)

answer = 0
for i in range(n):
    for j in range(m):
        if visit_matrix[i][j]:
            answer += 1

print(answer)

    