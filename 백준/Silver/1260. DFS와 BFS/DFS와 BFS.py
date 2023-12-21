import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

def DFS(nodes, visited, answer, now):
    next_arr = nodes[now]
    next_arr = sorted(next_arr)
    for num in next_arr:
        if visited[num] == "X":
            answer.append(num)
            visited[num] = "O"
            DFS(nodes, visited, answer, num)

N, M, start = map(int, input().split())
nodes = [[] for _ in range(N + 1)]
visited = ["X"] * (N + 1)

for _ in range(M):
    first, second = map(int, input().split())
    nodes[first].append(second)
    nodes[second].append(first)
    
answer1 = [start]
visited1 = visited[:]
visited1[start] = "O"
DFS(nodes, visited1, answer1, start)

queue = deque([start])
visited2 = visited[:]
visited2[start] = "O"
answer2 = []
while queue:
    now = queue.popleft()
    answer2.append(now)
    for num in sorted(nodes[now]):
        if visited2[num] == "X":
            visited2[num] = "O"
            queue.append(num)
        
for i in answer1:
    print(i, end = " ")
print()
for j in answer2:
    print(j, end = " ")