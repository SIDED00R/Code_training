t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for _ in range(n):
        line = list(map(int, input().split()))
        count = 0
        for idx in range(n):
            if line[-1 - idx] == 1:
                count += 1
            else:
                break
        l.append(count)
    sort_l = sorted(l, reverse = True)
    answer = 1
    while sort_l:
        out = sort_l.pop()
        if out >= answer:
            answer += 1
    print(min(answer, n))