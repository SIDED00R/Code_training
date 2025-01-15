import math

n = int(input())

l = []
for _ in range(n):
    name, num = input().split()
    l.append(float(num))

l.sort()
max_num = max(360 - l[-1] + l[0], l[1] - l[0])
for idx in range(n - 1):
    max_num = max(max_num, l[idx + 1] - l[idx])

print(math.ceil((360 - max_num) * 12))
