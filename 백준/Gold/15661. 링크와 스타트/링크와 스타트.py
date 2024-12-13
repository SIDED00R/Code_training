from itertools import product

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] += matrix[j][i]


answer = 1e9
for now_case in (list(product([0, 1], repeat = n))):
    if sum(now_case) in [0, 1, n - 1, n]:
        continue
    else:
        first_case = []
        second_case = []
        for idx in range(n):
            if now_case[idx] == 1:
                first_case.append(idx)
            else:
                second_case.append(idx)
        first_total = 0
        second_total = 0
        for i in range(len(first_case)):
            for j in range(i + 1, len(first_case)):
                first_total += matrix[first_case[i]][first_case[j]]
        for i in range(len(second_case)):
            for j in range(i + 1, len(second_case)):
                second_total += matrix[second_case[i]][second_case[j]]
        if answer > abs(first_total - second_total):
            answer = abs(first_total - second_total)

print(answer)