from collections import defaultdict

dic = defaultdict(list)

n = int(input())
matrix = []
for i in range(n):
    line = list(input())
    matrix.append(line)
    for j in range(n):
        if line[j] == 'Y':
            dic[i].append(j)
            dic[j].append(i)
            
count = [0 for _ in range(n)]
for i in range(n):
    visited = [False for _ in range(n)]
    visited[i] = True
    next_nodes = dic[i]
    for next_node in next_nodes:
        visited[next_node] = True
        for last_node in dic[next_node]:
            visited[last_node] = True
    count[i] = sum(visited) - 1

print(max(count))
    