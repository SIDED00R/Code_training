from collections import defaultdict


n = int(input())
a = defaultdict(list)
a[0].append(0)

x = 1
while n >= x:
    a[x].append(x)
    n -= x
    x += 1
if n:
    a[n].append(x)

ans = []
for i in range(1, 100000):
    for j in a[i]:
        ans.append((j, a[i-1][-1]))
ans.append((0, -1))

print(len(ans))
for xx, yy in ans:
    print(xx, yy)


