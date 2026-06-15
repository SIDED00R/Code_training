from collections import defaultdict
import sys
input = sys.stdin.readline

def find(node, route):
    able = True
    stack = [node]
    while stack:
        now = stack.pop()
        if len(route[now]) != 2:
            able = False
        for next_node in route[now]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

    return able

n, m = map(int, input().split())
route = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    route[a].append(b)
    route[b].append(a)

answer = 0
visited = [False] * (n + 1)
for now in range(1, n + 1):
    if visited[now]:
        continue
    else:
        visited[now] = True
        if find(now, route):
            answer += 1

print(answer)