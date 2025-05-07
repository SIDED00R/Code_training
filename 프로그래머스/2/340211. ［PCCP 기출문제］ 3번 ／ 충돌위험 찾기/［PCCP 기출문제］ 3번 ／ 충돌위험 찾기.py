from collections import defaultdict

def find_route(start, end):
    sx, sy = start
    ex, ey = end
    answer = []
    while True:
        if sx == ex and sy == ey:
            break
        answer.append((sx, sy))
        if sx > ex:
            sx -= 1
            continue
        elif sx < ex:
            sx += 1
            continue
        else:
            if sy > ey:
                sy -= 1
                continue
            elif sy < ey:
                sy += 1
                continue
    return answer

def solution(points, routes):
    dic = {}
    for idx, point in enumerate(points):
        dic[idx + 1] = point[:]
        
    cases = []
    for route in routes:
        now_case = []
        for idx in range(1, len(route)):
            before = route[idx - 1]
            after = route[idx]
            now_case.extend(find_route(dic[before], dic[after]))
        now_case.append(tuple(dic[route[-1]]))
        cases.append(now_case)
    find = True
    idx = 0
    ans = 0
    while find:
        find = False
        dic = defaultdict(int)
        for nc in cases:
            if len(nc) > idx:
                find = True
                dic[nc[idx]] += 1
        for k, v in dic.items():
            if v >= 2:
                ans += 1
        idx += 1
    return ans