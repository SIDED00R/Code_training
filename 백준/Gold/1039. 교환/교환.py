def change(l):
    length = len(l)
    answer = set()
    for i in range(length):
        for j in range(i + 1, length):
            now_l = l[:]
            now_l[i], now_l[j] = now_l[j], now_l[i]
            answer.add(tuple(now_l))
    return answer
            
n, k = input().split()
k = int(k)

n = list(map(int, n))

if len(n) == 1 or (len(n) == 2 and n[-1] == 0):
    print(-1)
    exit()

now_able = {tuple(n)}

for _ in range(k):
    next_able = set()
    for now_case in now_able:
        next_able.update(change(list(now_case)))
    now_able = next_able

answer = 0
for now_case in now_able:
    answer = max(answer, int("".join(list(map(str, now_case)))))

print(answer)