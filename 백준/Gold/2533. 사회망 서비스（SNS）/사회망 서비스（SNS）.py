from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(now_node):
    for next_node in connect[now_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)
            dp[now_node][0] += dp[next_node][1]
            dp[now_node][1] += min(dp[next_node])

n = int(input())
connect = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

visited = [False for _ in range(n + 1)]
dp = [[0, 1] for _ in range(n + 1)]
visited[1] = True
dfs(1)
print(min(dp[1]))