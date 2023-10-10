import sys

N = int(input())

s = set()

for i in range(N):
    line = sys.stdin.readline().split()
    if line[0] == "add":
        s.add(int(line[1]))

    elif line[0] == "remove":
        s.discard(int(line[1]))

    elif line[0] == "check":
        if int(line[1]) in s:
            print(1)
        else:
            print(0)

    elif line[0] == "toggle":
        if int(line[1]) in s:
            s.discard(int(line[1]))
        else:
            s.add(int(line[1]))

    elif line[0] == "all":
        s = set(range(1, 21))

    elif line[0] == "empty":
        s = set()
