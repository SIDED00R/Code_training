import sys

input = sys.stdin.readline
N, M = map(int, input().split())

nodes = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    u, v = map(int, input().split())
    nodes[u - 1].append(v - 1)
    nodes[v - 1].append(u - 1)

answer = 0
for i in range(N):
    if visited[i]:
        continue
    else:
        answer += 1
        visited[i] = True
        stack = nodes[i]
        while stack:
            next_node_idx = stack.pop()
            if visited[next_node_idx]:
                continue
            else:
                stack += nodes[next_node_idx]
                visited[next_node_idx] = True
            
print(answer)
            
    