n = int(input())
goal = []
for _ in range(n):
    x, y = map(int, input().split())
    goal.append([x, y])

m = int(input())
dic = {}
for _ in range(m):
    x, y = map(int, input().split())
    dic[(x, y)] = 1
    
start_x, start_y = goal[0]

for key, _ in dic.items():
    now_x, now_y = key
    ans_x = now_x - start_x
    ans_y = now_y - start_y
    find = True
    for case in goal:
        case_x, case_y = case
        case_x += ans_x
        case_y += ans_y
        if (case_x, case_y) in dic:
            continue
        else:
           find = False
           break
    if find:
        print(ans_x, ans_y)
        break

