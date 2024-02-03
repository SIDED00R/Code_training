from math import inf
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
nodes = [[] for _ in range(N + 1)]
for _ in range(M):
    now_num, next_num, cost = map(int, input().rstrip('\n').split())
    nodes[now_num].append({next_num: cost})

start, end = map(int, input().rstrip('\n').split())
stack = deque([start])
node_count = [inf] * (N + 1)
node_count[start] = 0
visited = [False] * (N + 1)
now = start

stack = set()
while True:
    for case in nodes[now]:
        for key, value in case.items():
            if not visited[key]:
                if node_count[key] > node_count[now] + value:
                    node_count[key] = node_count[now] + value
                    stack.add(key)
    visited[now] = True
    
    min_node_count = inf
    for idx in stack:
        if min_node_count > node_count[idx]:
            min_node_count = node_count[idx]
            now = idx
    stack.remove(now)
    if now == end:
        break

print(node_count[end])
    
    