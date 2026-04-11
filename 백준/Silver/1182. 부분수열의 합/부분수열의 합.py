n, s = map(int, input().split())
line = list(map(int, input().split()))
answer = 0
for now in range(1, 1 << n):
    total = 0
    for idx in range(n):
        if (2 ** idx) & now == (2 ** idx):
            total += line[idx]
    if total == s:
        answer += 1

print(answer)