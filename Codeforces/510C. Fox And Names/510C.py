from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

graph = [[] for _ in range(26)]
indegree = [0] * 26
edge = [[False] * 26 for _ in range(26)]

possible = True

for i in range(n - 1):
    a = names[i]
    b = names[i + 1]

    found = False
    min_len = min(len(a), len(b))

    for j in range(min_len):
        if a[j] != b[j]:
            u = ord(a[j]) - ord('a')
            v = ord(b[j]) - ord('a')

            if not edge[u][v]:
                edge[u][v] = True
                graph[u].append(v)
                indegree[v] += 1

            found = True
            break

    if not found and len(a) > len(b):
        possible = False
        break

if not possible:
    print("Impossible")
else:
    q = deque()

    for i in range(26):
        if indegree[i] == 0:
            q.append(i)

    ans = []

    while q:
        now = q.popleft()
        ans.append(now)

        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    if len(ans) != 26:
        print("Impossible")
    else:
        print(''.join(chr(x + ord('a')) for x in ans))