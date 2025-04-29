import heapq

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(first, second):
    a = find(first)
    b = find(second)
    if a == b:
        return False
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return True


n, m = map(int, input().split())
stack = []
for _ in range(m):
    u, v, t = map(int, input().split())
    heapq.heappush(stack, [t, min(u, v), max(u, v)])

count = 1
parent = [i for i in range(n + 1)]
while stack:
    t, u, v = heapq.heappop(stack)
    if t != count:
        break
    if union(u, v):
        count += 1

print(count)
