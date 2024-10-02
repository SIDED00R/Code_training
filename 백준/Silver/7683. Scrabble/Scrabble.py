from collections import defaultdict
import copy

while True:
    n = int(input())
    answer = 0

    if n == 0:
        break
    dic = []
    for _ in range(n + 1):
        d = defaultdict(int)
        for alp in input():
            d[alp] += 1
        dic.append(d)
    check = dic.pop()
    key = 0
    if "_" in check:
        key = check["_"]
    for case in dic:
        now_check = copy.deepcopy(check)
        now_key = key
        find = True
        for k, v in case.items():
            if now_check[k] >= v:
                now_check[k] -= v
            else:
                left = v - now_check[k]
                now_check[k] = 0
                now_check["_"] -= left
            if now_check["_"] < 0:
                find = False
                break
        if find:
            answer += 1
    print(answer)

