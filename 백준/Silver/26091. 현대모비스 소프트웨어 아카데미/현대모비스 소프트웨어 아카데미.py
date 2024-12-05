import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
line = list(map(int, input().split()))
line = deque(sorted(line))

answer = 0
while len(line) >= 2:
    now = line.pop()
    while line:
        front = line.popleft()
        if now + front >= m:
            answer += 1
            break
print(answer)