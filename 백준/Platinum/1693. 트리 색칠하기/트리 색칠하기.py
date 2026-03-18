import math
from collections import defaultdict
n = int(input())
weight = [i + 1 for i in range(n)]
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
child = defaultdict(list)
while stack:
    out = stack.pop()
    for next_node in route[out]:
        if not visited[next_node]:
            visited[next_node] = True
            child[out].append(next_node)
            stack.append(next_node)
            keep.append(next_node)

length = int(math.log2(n)) + 1
dp = [[1e10 for _ in range(length)] for _ in range(n)]
while keep:
    out = keep.pop()
    for idx in range(length):
        select = weight[idx]
        for next_node in child[out]:
            select += min(dp[next_node][:idx] + dp[next_node][idx + 1:])
        dp[out][idx] = select

print(min(dp[0]))