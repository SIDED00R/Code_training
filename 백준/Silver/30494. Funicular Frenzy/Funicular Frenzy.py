n, c = map(int, input().split())
line = list(map(int, input().split()))
answer = -1
min_wait_time = n + 1
total = 0
for idx, num in enumerate(line):
    total += num
    if total < c:
        print(idx)
        exit()
    else:
        able = total // c
        if idx + 1 + able > n:
            break
        else:
            if min_wait_time > able:
                answer = idx
                min_wait_time = able
        total -= c
if answer == -1:
    print("impossible")
else:
    print(answer)