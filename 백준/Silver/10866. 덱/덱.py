import sys

n = int(input())
stack = []
for _ in range(n):
    order = sys.stdin.readline().split()
    f = order[0]
    if f == "push_front":
        stack.insert(0, order[1])
    elif f == "push_back":
        stack.append(int(order[1]))
    elif f == "pop_front":
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop(0)
            print(num)
    elif f == "pop_back":
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop()
            print(num)
    elif f == "size":
        print(len(stack))
    elif f == "empty":
        print(int(len(stack) == 0))
    elif f == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif f == "back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])