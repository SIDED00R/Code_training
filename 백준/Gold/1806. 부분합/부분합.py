import sys
input = sys.stdin.readline
from collections import deque


N, S = map(int, input().rstrip('wn').split())
line = list(map(int, input().rstrip('wn').split()))
stack = deque()
total = 0
answer = N + 1
for num in line:
    stack.append(num)
    total += num
    while total >= S:
        if answer > len(stack):
            answer = len(stack)
        out = stack.popleft()
        total -= out
        
print(0) if answer == N + 1 else print(answer)