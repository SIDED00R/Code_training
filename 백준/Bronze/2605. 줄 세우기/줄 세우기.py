n = int(input())
line = list(map(int, input().split()))
stack = []
for num in range(n):
    idx = line[num]
    if idx == 0:
        stack.append(num + 1)
    else:
        front = stack[:-idx]
        back = stack[-idx:]
        stack = front + [num + 1] + back

print(*stack)