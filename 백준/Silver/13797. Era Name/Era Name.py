while True:
    n, m = map(int, input().split())
    dic = {}
    if n == 0 and m == 0:
        break
    for _ in range(n):
        name, y, year = input().split()
        dic[name] = [int(year) - int(y) + 1, int(year)]

    for _ in range(m):
        find = False
        now = int(input())
        for k, v in dic.items():
            if v[0] <= now <= v[1]:
                find = True
                print(k, now - v[0] + 1)
                break
        if find:
            continue
        else:
            print("Unknown")