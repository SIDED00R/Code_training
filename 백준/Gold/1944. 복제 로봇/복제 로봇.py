import sys
from collections import deque
from itertools import combinations
import heapq

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(num_a, num_b):
    queue = deque([[node[num_a][0], node[num_a][1], 0]]) # start -> x, y, 0
    visited = [[False] * N for _ in range(N)]
    visited[node[num_a][0]][node[num_a][1]] = True

    while queue:
        x, y, d = queue.popleft()
        if x == node[num_b][0] and y == node[num_b][1]: # arrived?
            return d

        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0 <= ax <= N - 1 and 0 <= ay <= N - 1 and not visited[ax][ay] and mat[ax][ay] != '1':
                visited[ax][ay] = True
                queue.append([ax, ay, d + 1])


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r2] = r1

N, K = map(int, sys.stdin.readline().split())

#init
cost, edges, c = 0, 0, 0 # c : # of nodes
graph, mat, node = [], [], []

for _ in range(N):
    mat.append(sys.stdin.readline().strip())

for i in range(N):
    for j in range(N):
        if mat[i][j] == 'S' or mat[i][j] == 'K':
            node.append((i, j))
            c += 1

p = [i for i in range(c)]

for a, b in combinations(range(c), 2):
        w = BFS(a, b)
        if w is None:
            print(-1)
            exit(0)
        heapq.heappush(graph, (w, a, b))

while True:
    if edges == len(node) - 1:
        break
    if not graph:
        print(-1)
        exit(0)
    w, a, b = heapq.heappop(graph)
    if find(a) != find(b):
        union(a, b)
        cost += w
        edges += 1
print(cost)