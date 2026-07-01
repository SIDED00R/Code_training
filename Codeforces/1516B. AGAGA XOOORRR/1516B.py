t = int(input())
for _ in range(t):
    n = int(input())
    n_l = list(map(int, input().split()))
    total = 0
    for num in n_l:
        total ^= num
    if total == 0:
        print("YES")
    else:
        find = False
        sign = False
        sub = 0
        for idx in range(n - 1):
            sub ^= n_l[idx]
            if sub == total:
                sign = True
            if sign and sub == 0:
                find = True
                break
        if find:
            print("YES")
        else:
            print("NO")