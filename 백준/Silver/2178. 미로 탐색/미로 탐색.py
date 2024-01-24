import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

maze = []
for _ in range(N):
    line = list(map(int, list(input())[:-1]))
    maze.append(line)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
count = 0
stack = deque([(0, 0, 1)])
while stack:
    now_i, now_j, now_num = stack.popleft()
    if now_i == N - 1 and now_j == M - 1:
        print(now_num)
    for idx in range(4):
        if 0 <= now_i + di[idx] < N and 0 <= now_j + dj[idx] < M and maze[now_i + di[idx]][now_j + dj[idx]] == 1:
            maze[now_i + di[idx]][now_j + dj[idx]] = 0
            stack.append((now_i + di[idx], now_j + dj[idx], now_num + 1))
  