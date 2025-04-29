from collections import deque

stack = deque()
n, k = map(int, input().split())
for num in range(1, n + 1):
    stack.append(num)

while len(stack) > k:
    first = stack.popleft()
    for _ in range(k - 1):
        stack.popleft()
    stack.append(first)

print(stack[0])