def fin(num):
    answer = []
    for p in range(1, int(num ** 0.5) + 1):
        if num % p == 0:
            answer.append([p, num // p])
    return answer

g = int(input())
answer = []
for now_case in fin(g):
    small, large = now_case
    a = (small + large) / 2
    b = (large - small) / 2
    if a == int(a) and b == int(b) and b != 0:
        answer.append(int(a))

if answer:
    for num in sorted(answer):
        print(num)

else:
    print(-1)