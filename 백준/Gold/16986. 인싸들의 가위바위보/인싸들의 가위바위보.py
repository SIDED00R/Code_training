from itertools import permutations

n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

ky = list(map(int, input().split()))
mi = list(map(int, input().split()))

able = False
for nc in permutations(range(1, n + 1)):
    now_case = list(nc)
    count = [0, 0, 0]
    now = [0, 1]
    left = 2
    l = [now_case, ky, mi]
    while True:
        front = now[0]
        back = now[1]
        if l[front] == [] or l[back] == []:
            break
        front_l = l[front]
        back_l = l[back]
        check = matrix[front_l[0] - 1][back_l[0] - 1]
        l[front] = front_l[1:]
        l[back] = back_l[1:]
        if check == 2:
            count[front] += 1
            now[1], left = left, now[1]
        else:
            count[back] += 1
            now[0], now[1], left = now[1], left, now[0]
        if now[0] > now[1]:
            now = now[::-1]
        if k in count:
            if count[0] == k:
                able = True
            break
    if able:
        break

if able:
    print(1)
else:
    print(0)
            