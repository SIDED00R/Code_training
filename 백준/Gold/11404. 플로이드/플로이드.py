import sys
input = sys.stdin.readline
from math import inf

n = int(input())
m = int(input())
citys = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    i, j, cost = map(int, input().rstrip('\n').split())
    citys[i][j] = min(citys[i][j], cost)
    
for i in range(n + 1):
    citys[i][i] = 0
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            citys[j][k] = min(citys[j][i] + citys[i][k], citys[j][k])
            
for line in citys[1:]:
    for num in line[1:]:
        if num != inf:
            print(num, end = " ")
        else:
            print(0, end = " ")
    print()