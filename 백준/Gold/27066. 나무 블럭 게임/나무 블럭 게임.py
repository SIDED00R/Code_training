n = int(input())
line = sorted(map(int, input().split()))
if n == 1:
    print(line[0])
else:
    print(max(line[-2], sum(line) / n))