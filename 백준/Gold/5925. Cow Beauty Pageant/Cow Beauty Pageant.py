import sys
from collections import deque

input = sys.stdin.read

def dst(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dfs(pos, arr, n, m, field, vit, dx, dy):
    stack = [pos]
    while stack:
        cur = stack.pop()
        vit[cur[0]][cur[1]] = True
        arr.append(cur)
        for i in range(4):
            np = (cur[0] + dx[i], cur[1] + dy[i])
            if np[0] < 0 or np[1] < 0 or np[0] >= n or np[1] >= m:
                continue
            if vit[np[0]][np[1]] or field[np[0]][np[1]] == '.':
                continue
            stack.append(np)

def setlen(num, a, b, comp, len_arr, route):
    for u in comp[a]:
        for v in comp[b]:
            if dst(u, v) - 1 < len_arr[num]:
                len_arr[num] = dst(u, v) - 1
                route[num].clear()
            if dst(u, v) - 1 == len_arr[num]:
                route[num].append((u, v))

def solve(from_idx, to_idx, route, comp, len_arr):
    global ans
    for u in route[from_idx]:
        sx = min(u[0][0], u[1][0])
        ex = max(u[0][0], u[1][0])
        sy = min(u[0][1], u[1][1])
        ey = max(u[0][1], u[1][1])
        for i in range(sx, ex + 1):
            for j in range(sy, ey + 1):
                for p in comp[to_idx]:
                    ans = min(ans, len_arr[from_idx] + dst((i, j), p) - 1)

def main():
    global ans
    data = input().split()
    n, m = int(data[0]), int(data[1])
    field = data[2:2+n]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    vit = [[False] * m for _ in range(n)]
    comp = []

    for i in range(n):
        for j in range(m):
            if vit[i][j] or field[i][j] == '.':
                continue
            route = []
            dfs((i, j), route, n, m, field, vit, dx, dy)
            comp.append(route)

    len_arr = [float('inf')] * 3
    route = [[] for _ in range(3)]

    setlen(0, 0, 1, comp, len_arr, route)
    setlen(1, 1, 2, comp, len_arr, route)
    setlen(2, 0, 2, comp, len_arr, route)

    temp = [len_arr[0], len_arr[1], len_arr[2]]
    temp.sort()
    ans = temp[0] + temp[1]

    solve(0, 2, route, comp, len_arr)
    solve(1, 0, route, comp, len_arr)
    solve(2, 1, route, comp, len_arr)

    print(ans)

if __name__ == "__main__":
    main()
