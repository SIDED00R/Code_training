import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)
    
count_small = N * N

for i in range(1, N + 1):
    stack = [i]
    new_stack = []
    visited = [False] * (N + 1)
    visited[i] = True
    count = 1
    total = 0
    
    while stack:
        now = stack.pop()
        for num in graph[now]:
            if not visited[num]:
                new_stack.append(num)
                visited[num] = True
                
        if stack == []:
            total += (count * len(new_stack))
            stack = new_stack[:]
            new_stack = []
            count += 1
            
    if total < count_small:
        count_small = total
        idx = i
        
print(idx)
        
    