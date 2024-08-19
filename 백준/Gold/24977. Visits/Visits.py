def find(node):
    if parents_node[node] != node:
        parents_node[node] = find(parents_node[node])
    return parents_node[node]

def union(first, second):
    second_root = find(second)
    parents_node[first] = second_root

n = int(input())
weight = [0]
edge = [0]
parents_node = [i for i in range(n + 1)]
for i in range(1, n + 1):
    a, v = map(int, input().split())
    weight.append(v)
    edge.append(a)
    union(i, a)
    
answer = sum(weight)
for i in range(1, n + 1):
    if parents_node[i] == i:
        min_weight = weight[i]
        next_i = edge[i]
        while True:
            if next_i == i:
                break
            else:
                min_weight = min(min_weight, weight[next_i])
            next_i = edge[next_i]
        answer -= min_weight
        
print(answer)