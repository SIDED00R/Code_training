from collections import deque

def check(x, y, idx, r):
    dx, dy = able[idx]
    diff = (x - dx) ** 2 + (y - dy) ** 2
    if diff <= r ** 2:
        return True
    return False

n, r, d, x, y = map(int, input().split())

able = []
visited = [False for _ in range(n)]
for _ in range(n):
    i, j = map(int, input().split())
    able.append([i, j])

answer = 0
stack = deque([[x, y, 0]])
while stack:
    i, j, w = stack.popleft()
    for idx in range(n):
        if not visited[idx] and check(i, j, idx, r):
            visited[idx] = True
            answer += d / 2 ** w
            stack.append([able[idx][0], able[idx][1], w + 1])

print(answer)