n = int(input())
first = list(map(int, list(input())))
second = list(map(int, list(input())))
answer = []
if sum(first) == n:
    total = sum(second)
    print(total * (total - 1) + 1)
else:
    keep = 0
    start = -1
    end = -1
    for idx in range(n):
        if first[idx] == 1 and keep == 0:
            keep = 1
            start = idx
        elif keep == 1 and first[idx] == 0:
            keep = 0
            answer.append([start, idx - 1])
    if start > end:
        answer.append([start, idx])

    front = answer[0]
    back = answer[-1]
    if front[0] == 0 and back[1] == n - 1:
        answer.pop()
        answer[0] = [back[0], front[1]]
        
    ans_num = 0
    for now_case in answer:
        f, b = now_case
        count = 0
        if f > b:
            for i in range(f - 1, n):
                if second[i] == 1:
                    count += 1
            for i in range(b + 1):
                if second[i] == 1:
                    count += 1
        else:
            for i in range(f - 1, b + 1):
                if second[i] == 1:
                    count += 1
        ans_num += count * (count - 1) // 2
    print(ans_num)