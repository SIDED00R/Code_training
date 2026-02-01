n, m = map(int, input().split())
k = int(input())
dic = {}
for _ in range(k):
    a, b, c, d = map(int, input().split())
    min_cord = min([a, b], [c, d])
    max_cord = max([a, b], [c, d])
    dic[tuple(min_cord + max_cord)] = 1

matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
matrix[0][0] = 1

for i in range(1, n + 1):
    if (i - 1, 0, i, 0) in dic:
        continue
    else:
        matrix[i][0] = matrix[i - 1][0]

for j in range(1, m + 1):
    if (0, j - 1, 0, j) in dic:
        continue
    else:
        matrix[0][j] = matrix[0][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        now = 0
        if (i - 1, j, i, j) not in dic:
            now += matrix[i - 1][j]
        if (i , j - 1, i, j) not in dic:
            now += matrix[i][j - 1]
        matrix[i][j] = now

print(matrix[-1][-1])