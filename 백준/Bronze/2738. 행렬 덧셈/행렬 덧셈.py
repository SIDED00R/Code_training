import sys
input = sys.stdin.readline
N ,M = map(int, input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(2):
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            matrix[i][j] += line[j]

for arr in matrix:
    arr = list(map(str, arr))
    print(" ".join(arr))