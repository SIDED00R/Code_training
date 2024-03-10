import sys
input = sys.stdin.readline
from math import inf

N = int(input())
rgb_map = []
for i in range(N):
    line = list(map(int, input().rstrip('\n').split()))
    rgb_map.append(line)
    
answer = inf
for start in range(3):
    dp = [[inf for _ in range(3)] for _ in range(N)]
    dp[0][start] = rgb_map[0][start]
    for i in range(1, N - 1):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + rgb_map[i][j]
    for j in range(3):
        if start != j:
            dp[-1][j] = min(dp[-2][(j + 1) % 3], dp[-2][(j + 2) % 3]) + rgb_map[-1][j]
    for num in dp[-1]:
        if answer > num:
            answer = num

print(answer)