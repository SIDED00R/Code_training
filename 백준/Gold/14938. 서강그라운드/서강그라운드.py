import sys
input = sys.stdin.readline
from math import inf

n, m, r = map(int, input().rstrip('\n').split())
node_items = [0] + list(map(int, input().rstrip('\n').split()))

load_weight = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().rstrip('\n').split())
    load_weight[a].append([b, l])
    load_weight[b].append([a, l])

answer = 0
for idx in range(1, n + 1):
    visited = [inf] * (n + 1)
    visited[idx] = 0
    stack = [[idx, 0]]
    while stack:
        now_idx, now_weight = stack.pop()
        for case in load_weight[now_idx]:
            next_idx, next_weight = case
            added_weight = now_weight + next_weight
            if added_weight <= m and visited[next_idx] > added_weight:
                visited[next_idx] = added_weight
                stack.append([next_idx, added_weight])
    count_items = 0
    for visited_idx, num in enumerate(visited):
        if num != inf:
            count_items += node_items[visited_idx]
            
    if answer < count_items:
        answer = count_items
        
print(answer)