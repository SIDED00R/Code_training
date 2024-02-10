import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
if n == 1:
    print(0)
    exit()
nodes = [[] for _ in range(n + 1)]
parent_nodes = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(n - 1):
    parent, child, weight = map(int, input().rstrip('\n').split())
    parent_nodes[child].append((parent, weight))
    nodes[parent].append(child)
   
leaf_nodes = deque()
not_leaf_nodes = []
node_length = [0] * (n + 1)
for idx in range(1, n + 1):
    if not nodes[idx]:
        leaf_nodes.append(idx)
        node_length[idx] = parent_nodes[idx][0][1]
    else:
        not_leaf_nodes.append(idx)
        
if len(leaf_nodes) == 1:
    isline = True
else:
    isline = False
    
while leaf_nodes:
    now = leaf_nodes.popleft()
    parent = parent_nodes[now][0][0]
    if parent == 1:
        continue
    if node_length[parent] < node_length[now] + parent_nodes[parent][0][1]:
        node_length[parent] = node_length[now] + parent_nodes[parent][0][1]
        leaf_nodes.append(parent)

if isline:
    print(max(node_length))
else:
    while not_leaf_nodes:
        now = not_leaf_nodes.pop()
        if len(nodes[now]) < 2:
            continue
        first_max = 0
        second_max = 0
        for idx in nodes[now]:
            if node_length[idx] > second_max:
                second_max = node_length[idx]
            if second_max > first_max:
                first_max, second_max = second_max, first_max
        answer[now] = first_max + second_max
    print(max(answer + node_length))
    
