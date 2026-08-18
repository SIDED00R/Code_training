import sys
data = sys.stdin.buffer.read().split()
idx = 0
t = int(data[idx]); idx += 1
out = []

for _ in range(t):
    n = int(data[idx]); idx += 1

    L = [0] * (n + 1)
    R = [0] * (n + 1)
    for i in range(1, n + 1):
        L[i] = int(data[idx]); R[i] = int(data[idx + 1]); idx += 2

    deg = [0] * (n + 2)
    us = [0] * (n - 1)
    vs = [0] * (n - 1)
    for i in range(n - 1):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        us[i] = u; vs[i] = v
        deg[u] += 1; deg[v] += 1

    start = [0] * (n + 2)
    for i in range(1, n + 1):
        start[i + 1] = start[i] + deg[i]
    pos = start[:]
    adj = [0] * (2 * (n - 1))
    for i in range(n - 1):
        u = us[i]; v = vs[i]
        adj[pos[u]] = v; pos[u] += 1
        adj[pos[v]] = u; pos[v] += 1

    parent = [0] * (n + 1)
    order = [0] * n
    order[0] = 1
    head, cnt = 0, 1
    while head < cnt:
        node = order[head]; head += 1
        p = parent[node]
        for j in range(start[node], start[node + 1]):
            w = adj[j]
            if w != p:
                parent[w] = node
                order[cnt] = w; cnt += 1

    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    for i in range(n - 1, 0, -1):
        node = order[i]
        p = parent[node]
        nl = L[node]; nr = R[node]
        a = dp0[node]; b = dp1[node]
        l = L[p]; r = R[p]
        if a + abs(l - nl) > b + abs(l - nr):
            dp0[p] += a + abs(l - nl)
        else:
            dp0[p] += b + abs(l - nr)
        if a + abs(r - nl) > b + abs(r - nr):
            dp1[p] += a + abs(r - nl)
        else:
            dp1[p] += b + abs(r - nr)

    out.append(dp0[1] if dp0[1] > dp1[1] else dp1[1])

sys.stdout.write('\n'.join(map(str, out)))