import sys
input = sys.stdin.readline
from math import inf

N, M, X = map(int, input().rstrip('\n').split())
nodes = [{} for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, input().rstrip('\n').split())
    nodes[start][end] = time
    
go_weight = [inf] * (N + 1)
for i in range(1, N + 1):
    now = i
    weight = [inf] * (N + 1)
    visited = [False] * (N + 1)
    weight[now] = 0
    stack = set()
    
    while True:
        for end_node, value in nodes[now].items():
            if weight[end_node] > weight[now] + value:
                weight[end_node] = weight[now] + value
                stack.add(end_node)
        visited[now] = True
        
        min_weight = inf
        next_idx = 0
        for idx in stack:
            if min_weight > weight[idx]:
                min_weight = weight[idx]
                next_idx = idx
                
        if min_weight > weight[X]:
            go_weight[i] = weight[X]
            break
        else:
            now = next_idx
            stack.remove(now)
            
return_weight = [inf] * (N + 1)
return_weight[X] = 0
stack = [X]
while stack:
    now = stack.pop()
    for end_node, value in nodes[now].items():
        if return_weight[end_node] > return_weight[now] + value:
            stack.append(end_node)
            return_weight[end_node] = return_weight[now] + value
  
answer = 0
for i in range(1, N + 1):
    if go_weight[i] + return_weight[i] > answer:
        answer = go_weight[i] + return_weight[i]
        
print(answer)

    