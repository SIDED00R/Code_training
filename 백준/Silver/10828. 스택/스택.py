import sys

n = int(input())
stack = []

for _ in range(n):
    order = sys.stdin.readline().split()
    f = order[0]
    if f == "push":
        stack.append(int(order[1]))
    elif f == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif f == "size":
        print(len(stack))
    elif f == "empty":
        print(int(len(stack) == 0))
    elif f == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

