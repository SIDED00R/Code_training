n = int(input())
m = int(input())
bus = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]
road = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    bus[s][e] = min(bus[s][e], w)
    road[s][e] = [s, e]

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if start == end:
                continue
            if bus[start][end] > bus[start][mid] + bus[mid][end]:
                bus[start][end] = bus[start][mid] + bus[mid][end]
                road[start][end] = road[start][mid][:] + road[mid][end][1:]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if bus[i][j] == int(1e9):
            print(0, end = " ")
        else:
            print(bus[i][j], end = " ")
    print()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        count = len(road[i][j])
        if count == 0:
            print(0)
        else:
            print(count, end = " ")
            for node in road[i][j]:
                print(node, end = " ")
            print()
