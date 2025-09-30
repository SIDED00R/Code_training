from collections import defaultdict

def check(c):
    n = len(c)
    inside = defaultdict(list)
    outside = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            fx, fy, fr = c[i]
            sx, sy, sr = c[j]
            length = abs(fx - sx) ** 2 + abs(fy - sy) ** 2
            if length > (fr + sr) ** 2:
                continue
            else:
                if fr > sr:
                    inside[i].append(j)
                    outside[j].append(i)
                else:
                    inside[j].append(i)
                    outside[i].append(j)
    return inside, outside

def find_circle(circle, x1, y1, first_r):
    first = -1
    for idx, now_circle in enumerate(circle):
        x, y, r = now_circle
        length = abs(x - x1) ** 2 + abs(y - y1) ** 2
        if length > r ** 2:
            continue
        else:
            if r < first_r:
                first = idx
                first_r = r
    return first

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    circle = []
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        circle.append([cx, cy, r])
    inside, outside = check(circle)
    first_r = 10000
    second_r = 10000
    first = find_circle(circle, x1, y1, first_r)
    second = find_circle(circle, x2, y2, second_r)

    f_depth = len(outside[first])
    s_depth = len(outside[second])

    first_list = [first for _ in range(f_depth + 1)]
    second_list = [second for _ in range(s_depth + 1)]

    for now_case in outside[first]:
        depth = len(outside[now_case])
        first_list[f_depth - depth] = now_case

    for now_case in outside[second]:
        depth = len(outside[now_case])
        second_list[s_depth - depth] = now_case

    if first_list[-1] != -1:
        first_list.append(-1)
    if second_list[-1] != -1:
        second_list.append(-1)
    
    answer = len(first_list) + len(second_list) - 2
    for idx, num in enumerate(first_list):
        if num in second_list:
            answer = second_list.index(num) + idx
            break

    print(answer)
    


        