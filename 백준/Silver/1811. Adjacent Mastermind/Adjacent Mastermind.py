from collections import defaultdict

while True:
    line = input()
    if line == "#":
        break
    ans, check = line.split()
    black, grey, white = 0, 0, 0
    n = len(ans)
    ans_find = [False] * n
    check_find = [False] * n
    for idx in range(n):
        if ans[idx] == check[idx]:
            ans_find[idx] = True
            check_find[idx] = True
            black += 1
    for idx in range(n):
        back = max(idx - 1, 0)
        front = min(idx + 1, n - 1)
        if not ans_find[idx]:
            if not check_find[back] and ans[idx] == check[back]:
                ans_find[idx] = True
                check_find[back] = True
                grey += 1
            elif not check_find[front] and ans[idx] == check[front]:
                ans_find[idx] = True
                check_find[front] = True
                grey += 1
    ans_dic = defaultdict(int)
    check_dic = defaultdict(int)
    for idx in range(n):
        ans_dic[ans[idx]] += 1
        check_dic[check[idx]] += 1
    total = 0
    for key, value in ans_dic.items():
        if key in check_dic:
            total += min(value, check_dic[key])
            
    print(f"{check}: {black} black, {grey} grey, {total - black - grey} white")
    