n = int(input())
l = [0 for _ in range(n + 1)]
l[0] = l[1] = 1

for idx in range(4, n + 1):
    if idx % 2 == 0:
        l[idx] = l[idx - 4] * 2 * (idx // 4 * 2 - 1)
    else:
        l[idx] = l[idx - 1]


print(l[-1])