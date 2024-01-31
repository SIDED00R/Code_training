import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().rstrip('\n').split())

stack = deque([(N, 1)])
cases = {}
cases[N] = 1
while stack:
    now, count = stack.popleft()
    if now * 10 + 1 <= M and (now * 10 + 1) not in cases:
        cases[now * 10 + 1] = count + 1
        stack.append((now * 10 + 1, count + 1))
    if now * 2 <= M and (now * 2) not in cases:
        stack.append((now * 2, count + 1)) 
        cases[now * 2] = count + 1
    if M in cases:
        break
if M in cases:
    print(cases[M])
else:
    print(-1)