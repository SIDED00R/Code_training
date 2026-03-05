from collections import defaultdict

n = int(input())
m = int(input())
child = defaultdict(list)
parent = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    child[a].append(b)
    parent[b].append(a)

for i in range(1, n + 1):
    count = 1
    c_visited = [0 for _ in range(n + 1)]
    c_visited[i] = 1
    c = [i]
    p = [i]
    while c:
        out = c.pop()
        for next_node in child[out]:
            if not c_visited[next_node]:
                c_visited[next_node] = 1
                c.append(next_node)
                count += 1
    p_visited = [0 for _ in range(n + 1)]
    p_visited[i] = 1
    while p:
        out = p.pop()
        for next_node in parent[out]:
            if not p_visited[next_node]:
                p_visited[next_node] = 1
                p.append(next_node)
                count += 1
    print(n - count)
                