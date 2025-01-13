n, k, m = map(int, input().split())
now_dong = m

answer = 0
while True:
    answer += 1
    if now_dong == ((k - 1) % n + 1):
        break
    elif ((k - 1) % n + 1) < now_dong:
        now_dong -= ((k - 1) % n + 1)
        n -= 1
    else:
        now_dong = n - ((k - 1) % n + 1) + now_dong
        n -= 1

print(answer)