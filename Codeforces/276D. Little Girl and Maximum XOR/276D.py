a, b = map(int, input().split())
idx = 0
while True:
    if 2 ** idx > b:
        break
    else:
        idx += 1

answer = 0
while idx > 0:
    idx -= 1
    now = 2 ** idx
    if (a & now) == (b & now):
        continue
    else:
        answer = now * 2 - 1
        break

print(answer)