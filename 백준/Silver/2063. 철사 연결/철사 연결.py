k = int(input())
for _ in range(k):
    n = int(input())
    line = sorted(list(map(float, input().split())))
    find = False
    while line:
        last = line.pop()
        total = sum(line)
        if last <= total:
            find = True
    if find:
        print('YES')
    else:
        print('NO')
