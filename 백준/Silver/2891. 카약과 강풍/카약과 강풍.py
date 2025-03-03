n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
bring = list(map(int, input().split()))

total = [1 for _ in range(n + 1)]
for bro in broken:
    total[bro] -= 1
for bri in bring:
    total[bri] += 1

for idx in range(n + 1):
    if total[idx] == 2:
        if total[idx - 1] == 0:
            total[idx - 1] = 1
            total[idx] = 1
        elif idx != n and total[idx + 1] == 0:
            total[idx + 1] = 1
            total[idx] = 1

ans = 0
for i in range(1, n + 1):
    if total[i] == 0:
        ans += 1

print(ans)