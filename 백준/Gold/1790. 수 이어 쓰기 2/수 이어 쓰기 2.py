n, k = map(int, input().split())
left = k
d = 0
while True:
    if 9 * (10 ** d) * (d + 1) >= left:
        break
    else:
        left -= 9 * (10 ** d) * (d + 1)
    d += 1

num = left // (d + 1)
now_num = int(10 ** d) + num - 1
idx = left % (d + 1)
if idx == 0:
    if now_num > n:
        print(-1)
    else:
        print(str(now_num)[-1])
else:
    if now_num + 1 > n:
        print(-1)
    else:
        print(str(now_num + 1)[idx - 1])
