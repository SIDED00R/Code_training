import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)
node = defaultdict(list)
for _ in range(n - 1):
    first, second = map(int, input().split())
    node[first].append(second)
    node[second].append(first)


parent = [0] * (n + 1)

depth = [0] * (n + 1)


queue = deque([1])
visited[1] = True
while queue:
    current = queue.popleft()
    for child in node[current]:
        if not visited[child]:
            visited[child] = True
            parent[child] = current
            depth[child] = depth[current] + 1
            queue.append(child)


def lca(a, b):

    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a

m = int(input())
for _ in range(m):
    first, second = map(int, input().split())
    print(lca(first, second))