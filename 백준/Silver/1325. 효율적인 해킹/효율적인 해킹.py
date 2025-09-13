import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N + 1)] 
for _ in range(M):
    A, B = map(int, input().split())
    g[B].append(A)

visited = [0] * (N + 1)
run_id = 0

def bfs(start: int) -> int:
    global run_id
    run_id += 1
    q = deque([start])
    visited[start] = run_id
    cnt = 1

    while q:
        u = q.popleft()
        for v in g[u]:
            if visited[v] != run_id:
                visited[v] = run_id
                cnt += 1
                q.append(v)
    return cnt

max_cnt = 0
ans = []

for s in range(1, N + 1):
    c = bfs(s)
    if c > max_cnt:
        max_cnt = c
        ans = [s]
    elif c == max_cnt:
        ans.append(s)

print(*sorted(ans))
