t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    total = sum(line)
    count = 0
    while n >= total:
        count += 1
        total *= 4
    print(count + 1)