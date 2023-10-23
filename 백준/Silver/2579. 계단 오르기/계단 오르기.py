N = int(input())
if N == 1:
    print(int(input()))
else:
    stair = [0] * 301
    stair[1] = int(input())
    stair[2] = int(input())
    best = [0]
    best.append(stair[1])
    best.append(stair[1] + stair[2])
    for i in range(3, N + 1):
        stair[i] = int(input())
        best.append(stair[i] + max(best[i - 2], best[i - 3] + stair[i - 1]))
    print(best[N])


    