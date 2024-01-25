import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

square = []
for _ in range(N):
    line = list(map(int, list(input())[:-1]))
    square.append(line)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
answer = []
for i in range(N):
    for j in range(N):
        if square[i][j]:
            stack = deque([(i, j)])
            square[i][j] = 0
            count = 0
            while stack:
                count += 1
                now_i, now_j = stack.popleft()
                for idx in range(4):
                    if 0 <= now_i + di[idx] < N and 0 <= now_j + dj[idx] < N and square[now_i + di[idx]][now_j + dj[idx]] == 1:
                        square[now_i + di[idx]][now_j + dj[idx]] = 0
                        stack.append((now_i + di[idx], now_j + dj[idx]))      
            answer.append(count)
            
answer.sort()
print(len(answer))
for num in answer:
    print(num)
            
