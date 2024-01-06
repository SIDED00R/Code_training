import sys
input = sys.stdin.readline

def check(visited):
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if not visited[i][j]:
                return False
    return True


m, n = map(int, input().split())

ground = []
visited = [[False for _ in range(m)] for _ in range(n)]

stack = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 1:
            stack.append([i, j])
            visited[i][j] = True
        elif line[j] == -1:
            visited[i][j] = True
    ground.append(line)

count = 0
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

if check(visited):
    print(count - 1)
else:
    print(-1)
