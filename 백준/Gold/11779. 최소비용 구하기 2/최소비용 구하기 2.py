import sys
input = sys.stdin.readline
from math import inf
from collections import deque

n = int(input())
m = int(input())

nodes = [{} for _ in range(n + 1)]
for _ in range(m):
    start, end, weight = map(int, input().rstrip('\n').split())
    if end in nodes[start]:
        nodes[start][end] = min(nodes[start][end], weight)
    else:
        nodes[start][end] = weight

answer_start, answer_end = map(int, input().rstrip('\n').split())

weight_map = [[inf] for _ in range(n + 1)]
weight_map[answer_start] = [0, answer_start]

stack = deque([answer_start])
while stack:
    now = stack.popleft()
    for next_node, weight in nodes[now].items():
        if weight_map[next_node][0] > weight_map[now][0] + weight:
            weight_map[next_node] = weight_map[now][:]
            weight_map[next_node][0] += weight
            weight_map[next_node].append(next_node)
            stack.append(next_node)
                
answer = weight_map[answer_end]
print(answer[0])
print(len(answer) - 1)
for num in answer[1:]:
    print(num, end = " ")
    
