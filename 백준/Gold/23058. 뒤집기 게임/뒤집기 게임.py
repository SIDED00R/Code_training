from itertools import product
import copy

n = int(input())
keep_matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    keep_matrix.append(line)

cases = list(product([0, 1], repeat = n))

answer = 100
for now_case_i in cases:
    for now_case_j in cases:
        matrix = copy.deepcopy(keep_matrix)
        for i in range(n):
            if now_case_i[i] == 1:
                for idx in range(n):
                    matrix[i][idx] = (matrix[i][idx] + 1) % 2
        for j in range(n):
            if now_case_j[j] == 1:
                for idx in range(n):
                    matrix[idx][j] = (matrix[idx][j] + 1) % 2

        total = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    total += 1
        total = min(total, n * n - total)
        answer = min(answer, total + sum(now_case_i) + sum(now_case_j))

print(answer)