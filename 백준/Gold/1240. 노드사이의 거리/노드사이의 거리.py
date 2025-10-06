from collections import defaultdict

n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]
dic = defaultdict(list)
weight = {}
for _ in range(n - 1):
    a, b, length = map(int, input().split())
    a -= 1
    b -= 1
    weight[(a, b)] = length
    weight[(b, a)] = length
    dic[a].append(b)
    dic[b].append(a)

for i in range(n):
    visited = [0 for _ in range(n)]
    visited[i] = 1
    stack = [[i, 0]]
    while stack:
        now_node, now_weight = stack.pop()
        for next_node in dic[now_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                w = weight[(now_node, next_node)]
                next_weight = now_weight + w
                matrix[i][next_node] = next_weight
                matrix[next_node][i] = next_weight
                stack.append([next_node, next_weight])

for _ in range(m):
    a, b = map(int, input().split())
    print(matrix[a - 1][b - 1])