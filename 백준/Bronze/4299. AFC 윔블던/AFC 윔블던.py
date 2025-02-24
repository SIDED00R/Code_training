add, sub = map(int, input().split())
if (add + sub) % 2 == 0:
    win = (add + sub) // 2
    lose = (add - sub) // 2
    if lose < 0:
        print(-1)
    else:
        print(f"{win} {lose}")
else:
    print(-1)