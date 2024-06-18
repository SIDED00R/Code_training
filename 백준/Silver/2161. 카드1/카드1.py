from collections import deque

n = int(input())
stack = deque([i for i in range(1, n + 1)])
answer = []
while stack:
    answer.append(stack.popleft())
    if stack:
        stack.append(stack.popleft())
for num in answer:
    print(num, end = " ")