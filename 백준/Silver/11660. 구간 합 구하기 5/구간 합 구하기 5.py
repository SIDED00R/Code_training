from ast import AsyncFunctionDef
from re import A
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
metrix = []
for _ in range(N):
    line = list(map(int, input().rstrip('\n').split()))
    metrix.append(line)

sum_metrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        now = metrix[i][j]
        if i > 0:
            now += sum_metrix[i - 1][j]
        if j > 0:
            now += sum_metrix[i][j - 1]
        if i > 0 and j > 0:
            now -= sum_metrix[i - 1][j - 1]
        sum_metrix[i][j] = now
        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip('\n').split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    answer = sum_metrix[x2][y2]
    if x1 > 0:
        answer -= sum_metrix[x1 - 1][y2]
    if y1 > 0:
        answer -= sum_metrix[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        answer += sum_metrix[x1 - 1][y1 - 1]
    print(answer)
