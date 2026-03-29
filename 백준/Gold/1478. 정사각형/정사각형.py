x = {}
y = {}
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) in x:
        x[(x1, y1)] = [max(x2, x[(x1, y1)][0]), y1]
    else:
        x[(x1, y1)] = [x2, y1]

    if (x1, y2) in x:
        x[(x1, y2)] = [max(x2, x[(x1, y2)][0]), y2]
    else:
        x[(x1, y2)] = [x2, y2]

    if (x1, y1) in y:
        y[(x1, y1)] = [x1, max(y2, y[(x1, y1)][1])]
    else:
        y[(x1, y1)] = [x1, y2]

    if (x2, y1) in y:
        y[(x2, y1)] = [x2, max(y2, y[(x2, y1)][1])]
    else:
        y[(x2, y1)] = [x2, y2]

new_x = []
for k in sorted(x, key=lambda d: (d[1], d[0])):
    sx, sy = k
    ex, ey = x[k]
    if not new_x:
        new_x.append([sx, sy, ex, ey])
    else:
        bsx, bsy, bex, bey = new_x[-1]
        if sy == bsy and sx <= bex:
            new_x[-1] = [bsx, bsy, max(bex, ex), bey]
        else:
            new_x.append([sx, sy, ex, ey])

new_y = []
for k in sorted(y, key=lambda d: (d[0], d[1])):
    sx, sy = k
    ex, ey = y[k]
    if not new_y:
        new_y.append([sx, sy, ex, ey])
    else:
        bsx, bsy, bex, bey = new_y[-1]
        if sx == bsx and sy <= bey:
            new_y[-1] = [bsx, bsy, bex, max(bey, ey)]
        else:
            new_y.append([sx, sy, ex, ey])

answer = 0
for i in range(1, len(new_x)):
    for j in range(i):
        isx, isy, iex, iey = new_x[i]
        jsx, jsy, jex, jey = new_x[j]

        diff = abs(jsy - isy)
        left = max(isx, jsx)
        right = min(iex, jex)

        if diff == 0 or right - left < diff:
            continue

        for yi in range(1, len(new_y)):
            for yj in range(yi):
                yisx, yisy, yiex, yiey = new_y[yi]
                yjsx, yjsy, yjex, yjey = new_y[yj]

                d = abs(yjsx - yisx)

                if diff == d and \
                   yisy <= isy <= yiey and yisy <= jsy <= yiey and \
                   yjsy <= isy <= yjey and yjsy <= jsy <= yjey and \
                   left <= yisx <= right and left <= yjsx <= right:
                    answer += 1

print(answer)