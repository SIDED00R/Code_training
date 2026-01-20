n = int(input())
for idx in range(1, n + 1):
    line = list(map(int, input().split()))
    if line == [i for i in range(1, 6)] * 2:
        print(idx)