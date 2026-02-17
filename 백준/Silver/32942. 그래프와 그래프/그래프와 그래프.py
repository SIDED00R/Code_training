a, b, c = map(int, input().split())
answer = [set() for _ in range(10)]
if b == 0:
    if a != 0 and c % a == 0:
        x0 = c // a
        if 1 <= x0 <= 10:
            answer[x0 - 1] = set(range(1, 11))
else:
    for x in range(1, 11):
        t = c - a * x
        if t % b == 0:
            y = t // b
            if 1 <= y <= 10:
                answer[x - 1].add(y)

for now in answer:
    if not now:
        print(0)
    else:
        print(*sorted(now))