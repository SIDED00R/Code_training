import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ground = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    now_line = []
    for j in range(m):
        if line[j] == 2:
            start_i = i
            start_j = j
        if line[j] == 0:
            visited[i][j] = True
            now_line.append(0)
        else:
            now_line.append(-1)
    ground.append(now_line)

visited[start_i][start_j] = True
count = 0
stack = [[start_i, start_j]]
next_stack = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
while stack:
    now_i, now_j = stack.pop()
    ground[now_i][now_j] = count
    for idx in range(4):
        next_i = now_i + di[idx]
        next_j = now_j + dj[idx]
        if next_i >= 0 and next_i < n and next_j >= 0 and next_j < m and not visited[next_i][next_j]:
            next_stack.append([next_i, next_j])
            visited[next_i][next_j] = True
    if not stack:
        stack = next_stack[:]
        count += 1
        next_stack = []     

for l in ground:
    print(" ".join(list(map(str, l))))