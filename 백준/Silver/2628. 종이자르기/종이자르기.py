n, m = map(int, input().split())
num = int(input())
row = []
col = []
for _ in range(num):
    check, idx = map(int, input().split())
    if check:
        col.append(idx)
    else:
        row.append(idx)

col = sorted(col)
row = sorted(row)

before_i = 0
max_i = 0
for i in col:
    max_i = max(max_i, i - before_i)
    before_i = i
max_i = max(max_i, n - before_i)

before_j = 0
max_j = 0
for j in row:
    max_j = max(max_j, j - before_j)
    before_j = j
max_j = max(max_j, m - before_j)

print(max_i * max_j)