import sys
input = sys.stdin.readline
import heapq
from math import inf

def find(start, end):
    visited = [False] * (N + 1)
    node_weight = [inf] * (N + 1)
    next_case = []
    heap = [[0, start]]
    while heap:
        now_weight, now_idx = heapq.heappop(heap)
        if visited[now_idx]:
            continue
        else:
            node_weight[now_idx] = now_weight
            for key, value in nodes[now_idx].items():
                if not visited[key]:
                    heapq.heappush(heap, [now_weight + value, key])
            visited[now_idx] = True
            
    return node_weight[1], node_weight[N], node_weight[end]
    

N, E = map(int, input().rstrip('\n').split())
nodes = {i:{} for i in range(1, N + 1)}
for _ in range(E):
    start, end, weight = map(int, input().rstrip('\n').split())
    nodes[start][end] = weight
    nodes[end][start] = weight

v1, v2 = map(int, input().rstrip('\n').split())

v1_1, v1_N, v1_v2 = find(v1, v2)
v2_1, v2_N, v2_v1 = find(v2, v1)
a, N_1, b = find(1, N)

answer = min(v1_1 + v1_v2 + v2_N, 
             v2_1 + v2_v1 + v1_N, 
             v1_1 + v1_N + 2 * v1_v2, 
             v2_1 + v2_N + v2_v1 * 2, 
             v1_1 * 2 + v2_1 + v2_N,
             v2_1 * 2 + v1_1 + v1_N,
             v1_1 * 2 + v2_1 * 2 + N_1
             )
if answer != inf:
    print(answer)
else:
    print(-1)