import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().rstrip('\n').split())
K = int(input())
nodes = {i:{} for i in range(1, V + 1)}
for _ in range(E):
    start, end, weight = map(int, input().rstrip('\n').split())
    try:
        if nodes[start][end] > weight:
            nodes[start][end] = weight
    except:
        nodes[start][end] = weight


visited = [False] * (V + 1)
node_weight = ["INF"] * (V + 1)
next_case = []

heap = [[0, K]]
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
        
for i in range(1, V + 1):
    print(node_weight[i])