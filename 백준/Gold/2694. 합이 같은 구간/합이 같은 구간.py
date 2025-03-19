def find(num):
    answer = set()
    for p in range(1, int(num ** 0.5) + 1):
        if num % p == 0:
            answer.add(p)
            answer.add(num // p)

    return answer


t = int(input())
for _ in range(t):
    m = int(input())
    line = []
    for _ in range((m - 1) // 10 + 1):
        line.extend(list(map(int, input().split())))
    able_case = sorted(find(sum(line)))
    
    for now_case in able_case:
        now_total = 0
        ans_find = True
        for idx in range(m):
            now_total += line[idx]
            if now_total < now_case:
                continue
            elif now_total == now_case:
                now_total = 0
            else:
                ans_find = False
                break
        if ans_find:
            print(now_case)
            break