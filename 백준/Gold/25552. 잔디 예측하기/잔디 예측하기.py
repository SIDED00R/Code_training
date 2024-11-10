n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

d = int(input())
direction = set()
for num_i in range(d + 1):
    for num_j in range(d + 1 - num_i):
        direction.add((num_i, num_j))
        direction.add((-num_i, num_j))
        direction.add((num_i, -num_j))
        direction.add((-num_i, -num_j))
pred_matrix = []
for _ in range(n):
    pred_matrix.append(list(input()))


stack = []
visited_matrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "O":
            if pred_matrix[i][j] == "X":
                print("NO")
                exit()
            stack.append([i, j])
            visited_matrix[i][j] = 1
            pred_matrix[i][j] = "X"

while stack:
    now_i, now_j = stack.pop()
    for d_case in direction:
        di, dj = d_case
        next_i = now_i + di
        next_j = now_j + dj
        if 0 <= next_i < n and 0 <= next_j < m and visited_matrix[next_i][next_j] == 0:
            visited_matrix[next_i][next_j] == 1
            if pred_matrix[next_i][next_j] == "O":
                pred_matrix[next_i][next_j] = "X"
                stack.append([next_i, next_j])

for i in range(n):
    for j in range(m):
        if pred_matrix[i][j] == "O":
            print("NO")
            exit()
print("YES")