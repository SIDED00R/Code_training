import sys

n = int(input())
now = 1
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    right = False
    if now >= 14:
        right = True
        now -= 13
    total = 0
    if right:
        for idx in range(len(line)):
            if idx % 2 == 0:
                if line[idx] >= now:
                    now += total
                    break
                else:
                    total += line[idx]
                    now -= line[idx]
            else:
                total += line[idx]
    else:
        for idx in range(len(line)):
            if idx % 2 == 1:
                if line[idx] >= now:
                    now += total
                    break
                else:
                    total += line[idx]
                    now -= line[idx]
            else:
                total += line[idx]

print(now)
