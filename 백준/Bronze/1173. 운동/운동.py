n, min_m, max_m, t, r = map(int, input().split())
answer = 0
count = 0
now_m = min_m
while True:
    answer += 1
    if now_m + t <= max_m:
        now_m += t
        count += 1
        if count == n:
            print(answer)
            exit()
    else:
        if now_m == min_m:
            print(-1)
            exit()
        now_m = max(min_m, now_m - r)
