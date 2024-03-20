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
 
def distance(first, second):
    f_x, f_y = first
    s_x, s_y = second
    return ((f_x - s_x) ** 2 + (f_y - s_y) ** 2) ** 0.5

n = int(input())
points = []
for _ in range(n):
    point = list(map(float, input().rstrip('\n').split()))
    points.append(point)
   
parents_node = [i for i in range(n)]
nodes = []
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        weight = distance(points[i], points[j])
        heapq.heappush(nodes, [weight, i, j])
        
answer = 0
count = 0
while count < n - 1:
    now_weight, now_start, now_end = heapq.heappop(nodes)
    if find(now_start) != find(now_end):  
        union(now_start, now_end)  
        answer += now_weight
        count += 1
               
print(round(answer, 2))