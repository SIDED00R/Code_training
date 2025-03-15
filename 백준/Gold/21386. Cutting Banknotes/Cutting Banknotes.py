t = int(input())
for _ in range(t):
    x = float(input())
    n = int(input())
    money = []
    for _ in range(n):
        money.append(int(input()))
    money = sorted(money)

    if (x * 4) != int(x * 4):
        print("no")
    else:
        if n >= 2:
            num = money[0]
            while num % 2 == 0:
                num //= 2
            find = False
            for now_num in money:
                if now_num % num == 0:
                    continue
                else:
                    find = True
                    exit
            if find:
                print("yes")
                exit()
        num = money[0]
        while num % 2 == 0:
            num //= 2
        if int(x * 4) % num == 0:
            print("yes")
        else:
            print("no")


