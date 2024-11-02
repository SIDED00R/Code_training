import sys
from collections import defaultdict
import heapq

n, m = map(int, input().split())
matrix = []
for i in range(n):
    line = list(sys.stdin.readline().rstrip('\n'))
    matrix.append(line)


sum_matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "D":
            sum_matrix[i + 1][j + 1] = 1
        sum_matrix[i + 1][j + 1] += (sum_matrix[i][j + 1] + sum_matrix[i + 1][j] - sum_matrix[i][j])

dic = defaultdict(int)
for i in range(n - m + 1):
    for j in range(n - m + 1):
        now = sum_matrix[i][j] + sum_matrix[i + m][j + m] - sum_matrix[i + m][j] - sum_matrix[i][j + m]
        dic[now] += 1


answer = []
for k, v in dic.items():
    heapq.heappush(answer, [k, v])

while answer:
    k, v = heapq.heappop(answer)
    print(k, v)