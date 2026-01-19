from itertools import permutations

def cycle(n, now):
    count = 0
    check = [False for _ in range(n)]
    for i in range(n):
        if check[i]:
            continue
        j = now[i]
        check[i] = True
        count += 1
        while not check[j]:
            check[j] = True
            j = now[j]
    return count
        

n = int(input())
matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)

for i in range(n):
    for j in range(n):
        if matrix[i][j].isalpha():
            matrix[i][j] = 64 - ord(matrix[i][j])
        else:
            matrix[i][j] = int(matrix[i][j])

min_value = 1e10
max_value = -1e10
for now in permutations(range(n), n):
    total = 1
    for i in range(n):
        j = now[i]
        total *= matrix[i][j]
    count = cycle(n, now)
    if count % 2 == 0:
        total *= -1
    min_value = min(min_value, total)
    max_value = max(max_value, total)

print(min_value)
print(max_value)
      