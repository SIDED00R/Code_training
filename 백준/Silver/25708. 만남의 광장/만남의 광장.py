from itertools import combinations

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

sum_col = [0] * m
sum_row = []
for i in range(n):
    sum_row.append(sum(matrix[i]))
    for j in range(m):
        sum_col[j] += matrix[i][j]

answer = -1e9
for row in combinations(range(n), 2):
    for col in combinations(range(m), 2):
        row1, row2 = row
        col1, col2 = col
        answer = max(answer, sum_col[col1] + sum_col[col2] + sum_row[row1] + sum_row[row2] - matrix[row1][col1] - matrix[row2][col1] - matrix[row1][col2] - matrix[row2][col2] + (row2 - row1 - 1) * (col2 - col1 - 1))
print(answer)