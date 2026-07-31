t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    max_num = max(line)
    if max_num * 2 > sum(line):
        print("T")
    else:
        if sum(line) % 2 == 0:
            print("HL")
        else:
            print("T")