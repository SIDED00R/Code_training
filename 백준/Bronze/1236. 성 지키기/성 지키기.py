n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

row_dic = {i:0 for i in range(n)}
col_dic = {j:0 for j in range(m)}
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "X":
            row_dic[i] = 1
            col_dic[j] = 1

count_row = 0
count_col = 0
for r_k, r_v in row_dic.items():
    if r_v == 0:
        count_row += 1
for c_k, c_v in col_dic.items():
    if c_v == 0:
        count_col += 1

print(max(count_row, count_col))