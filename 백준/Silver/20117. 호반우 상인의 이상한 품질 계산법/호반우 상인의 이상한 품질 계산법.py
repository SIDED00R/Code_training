n = int(input())
line = sorted(list(map(int, input().split())))
half = n // 2
if n % 2 == 0:
    print(2 * sum(line[-half:]))
else:
    print(2 * sum(line[-half:]) + line[half])