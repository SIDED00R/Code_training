def check(l, w, length):
    half = w / 2
    last_location = 0
    for num in l:
        start = num - half
        end = num + half
        if last_location == 0 and start > 0:
            return False
        if last_location >= start:
            last_location = end
        else:
            return False
    if last_location >= length:
        return True
    else:
        return False

while True:
    nx, ny, w = map(float, input().split())
    if nx == ny == w == 0:
        break
    xis = sorted(list(map(float, input().split())))
    yis = sorted(list(map(float, input().split())))
    if check(xis, w, 75) and check(yis, w, 100):
        print('YES')
    else:
        print('NO')