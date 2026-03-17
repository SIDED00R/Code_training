from collections import defaultdict
n = int(input())
weight = list(map(int, input().split()))
route = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    route[a].append(b)
    route[b].append(a)

visited = [False for _ in range(n)]
visited[0] = True
keep = [0]
stack = [0]
while stack:
    out = stack.pop()
    for next_node in route[out]:
        if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)
            keep.append(next_node)

dp = [[0, 0] for _ in range(n)]
while keep:
    out = keep.pop()
    n_select = 0
    select = weight[out]
    for next_node in route[out]:
        n_select += max(dp[next_node])
        select += dp[next_node][0]
    dp[out][0] = n_select
    dp[out][1] = select

print(max(dp[0]))