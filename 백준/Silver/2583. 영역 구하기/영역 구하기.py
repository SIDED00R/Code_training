m, n, k = map(int, input().split())
matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    matrix[ly][lx] += 1
    matrix[ry][rx] += 1
    matrix[ly][rx] -= 1
    matrix[ry][lx] -= 1

for i in range(m):
    for j in range(1, n):
        matrix[i][j] += matrix[i][j - 1]

for j in range(n):
    for i in range(1, m):
        matrix[i][j] += matrix[i - 1][j]

count = 0
answer = []
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
stack = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            count += 1
            stack.append([i, j])
            matrix[i][j] = 1
            total = 1
            while stack:
                ni, nj = stack.pop()
                for idx in range(4):
                    next_i = ni + di[idx]
                    next_j = nj + dj[idx]
                    if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] == 0:
                        matrix[next_i][next_j] = 1
                        total += 1
                        stack.append([next_i, next_j])
            answer.append(total)

answer.sort()

print(count)
for num in answer:
    print(num, end = " ")