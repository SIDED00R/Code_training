from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
a_list = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

b_list = list(map(int, input().split()))

stack = deque()
visited = [False for _ in range(n + 1)]
weight = [-1 for _ in range(n + 1)]
for b in b_list:
    stack.append([b, 0])
    visited[b] = True
    weight[b] = 0

while stack:
    node, w = stack.popleft()
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        else:
            visited[next_node] = True
            weight[next_node] = w + 1
            stack.append([next_node, w + 1])

answer_list = []
for idx in range(1, n + 1):
    if a_list[idx - 1] != 0 and weight[idx] == -1:
        print(-1)
        exit()
    answer_list.append(a_list[idx - 1] * weight[idx])

answer = sorted(answer_list)
print(sum(answer[-x:]))
