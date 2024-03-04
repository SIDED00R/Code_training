import sys
input = sys.stdin.readline
import heapq

def find(node):
    if parents_node[node] != node:
        parents_node[node] = find(parents_node[node])
    return parents_node[node]

def union(first, second):
    first_root = find(first)
    second_root = find(second)
    if first_root < second_root:
        parents_node[second_root] = first_root
    else:
        parents_node[first_root] = second_root

V, E = map(int, input().rstrip('\n').split())
parents_node = [i for i in range(V + 1)]
nodes = []
for _ in range(E):
    first, second, weight = map(int, input().rstrip('\n').split())
    heapq.heappush(nodes, [weight, first, second])

answer = 0    
count = 0
while count < V - 2:
    now_weight, now_start, now_end = heapq.heappop(nodes)
    if find(now_start) != find(now_end):  
        union(now_start, now_end)  
        answer += now_weight
        count += 1
               
print(answer)