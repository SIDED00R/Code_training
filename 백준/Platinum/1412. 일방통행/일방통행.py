def dfs(node, visited, stack, graph):
    visited[node] = 1
    stack[node] = 1  

    for neighbor in graph[node]:
        if stack[neighbor]: 
            return False
        if not visited[neighbor]:  
            if not dfs(neighbor, visited, stack, graph):
                return False

    stack[node] = 0 
    return True

n = int(input())

matrix = []
for _ in range(n):
    line = list(input())
    matrix.append(line)

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'Y' and matrix[j][i] == 'N':
            graph[i].append(j)

visited = [0] * n
stack = [0] * n

for i in range(n):
    if not visited[i]:
        if not dfs(i, visited, stack, graph):
            print("NO")
            exit()

print("YES")
