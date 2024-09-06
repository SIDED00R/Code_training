while True:
    f, s = map(int, input().split())
    if f == s == 0:
        break
    else:
        if f > s:
            print("Yes")
        else:
            print("No")