n = int(input())
line = list(map(int, input().split()))
if n == 2:
    print(min(line))
else:
    answer = 0
    for idx in range(n - 2):
        first, second, third = line[idx], line[idx + 1], line[idx + 2]
        now = sorted([first, second, third])
        answer = max(answer, now[1])
    print(answer)
