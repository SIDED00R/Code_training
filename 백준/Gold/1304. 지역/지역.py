def div(n):
    answer = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.append(i)
            if i ** 2 != n:
                answer.append(n // i)
    return sorted(answer)

n, m = map(int, input().split())
able_case = []

for _ in range(m):
    s, e = map(int, input().split())
    able_case.append([s, e])

div_case = div(n)

for now_case in div_case:
    size = n // now_case
    total = [0] * (n + 1)

    for i in range(1, n + 1):
        total[i] = (i - 1) // now_case + 1

    find = True
    for s, e in able_case:
        if total[s] > total[e]:
            find = False
            break
    if find:
        print(size)
        exit()