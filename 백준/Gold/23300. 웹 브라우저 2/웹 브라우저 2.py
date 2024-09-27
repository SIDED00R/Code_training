n, q = map(int, input().split())
back = []
front = []
now_page = ""
for _ in range(q):
    now = input()
    if now_page == "":
        if now[0] == "A":
            _, num = now.split()
            now_page = num
        continue

    if now == "B":
        if back:
            front.append(now_page)
            now_page = back.pop()

    elif now == "F":
        if front:
            back.append(now_page)
            now_page = front.pop()
    elif now == "C":
        if back:
            next_back = []
            for idx in range(len(back) - 1):
                if back[idx] == back[idx + 1]:
                    continue
                else:
                    next_back.append(back[idx])
            next_back.append(back[-1])
            back = next_back[:]
        else:
            continue
    else:
        front = []
        back.append(now_page)
        _, num = now.split()
        now_page = num

print(now_page)
if back:
    while back:
        b = back.pop()
        print(b, end = " ")
    print()
else:
    print(-1)
if front:
    while front:
        f = front.pop()
        print(f, end = " ")
else:
    print(-1)