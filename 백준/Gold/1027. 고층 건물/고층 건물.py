from collections import defaultdict

def able(i, j, dh):
    jh = line[j]
    if jh > line[i] + (j - i) * dh:
        return True, (line[j] - line[i]) / (j - i)
    else:
        return False, dh

n = int(input())
line = list(map(int, input().split()))

dic = defaultdict(int)
count = [0 for _ in range(n)]

for i in range(n):
    dh = -1e20
    for j in range(i + 1, n):
        check, dh = able(i, j, dh)
        if check:
            count[i] += 1
            count[j] += 1

print(max(count))