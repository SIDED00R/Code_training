n, m = map(int, input().split())
stack = []
for _ in range(m):
    stack.append(int(input()))

stack = sorted(stack)
max_value = 0
answer = -1
for idx in range(m):
    count = min(n, m - idx)
    if max_value < count * stack[idx]:
        max_value = count * stack[idx]
        answer = stack[idx]

print(answer, max_value)