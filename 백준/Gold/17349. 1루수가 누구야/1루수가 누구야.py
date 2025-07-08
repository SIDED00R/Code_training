import copy 

def check(now_l, idx):
    l = copy.deepcopy(now_l)
    l[idx][0] = (l[idx][0] + 1) % 2
    able = [-1] * 10
    for i in range(1, 10):
        tf, num = l[i]
        if tf == 1:
            if able[num] in [True, -1]:
                able[num] = True
            else:
                return -1
        else:
            if able[num] in [False, -1]:
                able[num] = False
            else:
                return -1

    t_count = 0
    ans = 0
    dont_know = 0
    dk_ans = 0
    for i in range(1, 10):
        now = able[i]
        if now == -1:
            dont_know += 1
            dk_ans = i
        elif now == True:
            t_count += 1
            ans = i
    if t_count > 1:
        return -1
    elif t_count == 1:
        return ans
    elif dont_know > 1:
        return -100
    elif dont_know == 1:
        return dk_ans
    else:
        return -1

l = [[0, 0]]
for _ in range(9):
    l.append(list(map(int, input().split())))

answer = -1
for i in range(1, 10):
    now = check(l, i)
    if now == -100:
        print(-1)
        exit()
    if now == -1:
        continue
    else:
        if answer == -1:
            answer = now
        else:
            if answer != now:
                print(-1)
                exit()

print(answer)