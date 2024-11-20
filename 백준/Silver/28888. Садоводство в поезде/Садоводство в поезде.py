n = int(input())
line = list(map(int, input().split()))
line = sorted(line, reverse = True)
maximum = 0
for idx in range(n):
    maximum = max(maximum, idx + line[idx])
print(maximum)