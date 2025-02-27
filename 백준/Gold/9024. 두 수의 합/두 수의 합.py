import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    line = sorted(list(map(int, input().split())))
    start = 0
    end = n - 1
    diff = abs(line[start] + line[end] - k)
    answer = 0
    while start < end:
        if abs(line[start] + line[end] - k) == diff:
            answer += 1
        elif abs(line[start] + line[end] - k) < diff:
            diff = abs(line[start] + line[end] - k)
            answer = 1

        if line[start] + line[end] - k <= 0:
            start += 1
        else:
            end -= 1

    print(answer)