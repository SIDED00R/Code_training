import sys

n = int(input())
que = []

for _ in range(n):
    order = sys.stdin.readline().split()
    f = order[0]
    if f == "push":
        que.append(int(order[1]))
    elif f == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    elif f == "size":
        print(len(que))
    elif f == "empty":
        print(int(len(que) == 0))
    elif f == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif f == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
