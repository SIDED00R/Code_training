from collections import defaultdict

idx = 0
while True:
    idx += 1
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    count = 0
    
    if n == m == 0:
        break
        
    route = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        route[a].append(b)
        route[b].append(a)

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            stack = [[i, -1]]
            find = True
            while stack:
                now_node, before_node = stack.pop()
                for next_node in route[now_node]:
                    if next_node == before_node:
                        continue
                    if visited[next_node] == True:
                        find = False
                    else:
                        visited[next_node] = True
                        stack.append([next_node, now_node])
            if find:
                count += 1
    if count == 1:
        print(f"Case {idx}: There is one tree.")
    elif count == 0:
        print(f"Case {idx}: No trees.")
    else:
        print(f"Case {idx}: A forest of {count} trees.")
                    