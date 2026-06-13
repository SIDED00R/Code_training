import sys
input = sys.stdin.readline

n, k = map(int, input().split())

route = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    route[u].append(v)
    route[v].append(u)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
subtree = [1] * (n + 1)

order = []
stack = [1]
parent[1] = -1

while stack:
    now = stack.pop()
    order.append(now)

    for nxt in route[now]:
        if nxt == parent[now]:
            continue
        parent[nxt] = now
        depth[nxt] = depth[now] + 1
        stack.append(nxt)

for now in reversed(order):
    if parent[now] != -1:
        subtree[parent[now]] += subtree[now]

value = []
for i in range(1, n + 1):
    value.append(depth[i] - subtree[i] + 1)

value.sort(reverse = True)
print(sum(value[:k]))