t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    print(min(line), max(line))