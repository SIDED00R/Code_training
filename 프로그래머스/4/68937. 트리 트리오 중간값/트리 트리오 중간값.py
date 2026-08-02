def solution(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # 1) BFS 순서 + 부모
    parent = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    visited[1] = True
    stack = [1]
    while stack:
        v = stack.pop()
        order.append(v)
        for w in adj[v]:
            if not visited[w]:
                visited[w] = True
                parent[w] = v
                stack.append(w)

    # 2) down[v] = v의 서브트리 아래 방향 최대 깊이 (역순 순회 = post-order)
    down = [0] * (n + 1)
    for v in reversed(order):
        for w in adj[v]:
            if w != parent[v] and down[w] + 1 > down[v]:
                down[v] = down[w] + 1

    # 3) up[v] = v에서 부모 방향으로의 최대 깊이 (정순 순회)
    up = [0] * (n + 1)
    ans = 0
    for v in order:
        b1 = b2 = 0
        arg1 = -1
        for w in adj[v]:
            if w == parent[v]:
                continue
            c = down[w] + 1
            if c > b1:
                b2, b1, arg1 = b1, c, w
            elif c > b2:
                b2 = c
        for w in adj[v]:
            if w == parent[v]:
                continue
            sib = b2 if w == arg1 else b1   # w 제외한 형제 중 최대
            up[w] = 1 + max(up[v], sib)

        # 4) v에서의 모든 가지 깊이 상위 3개 → d1 + d3
        d1 = d2 = d3 = 0
        cnt = 0
        for w in adj[v]:
            c = up[v] if w == parent[v] else down[w] + 1
            cnt += 1
            if c > d1:   d3, d2, d1 = d2, d1, c
            elif c > d2: d3, d2 = d2, c
            elif c > d3: d3 = c
        if cnt >= 2:          # 가지 2개 미만이면 median vertex가 될 수 없음
            ans = max(ans, d1 + d3)

    return ans