from collections import defaultdict

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    visited = [False] * len(a)
    graph = [[] for _ in range(len(a))]
    dic = defaultdict(int)
    for edge in edges:
        first, second = edge
        graph[first].append(second)
        graph[second].append(first)
        dic[first] += 1
        dic[second] += 1
    stack = []
    for key, value in dic.items():
        if value == 1:
            stack.append(key) 
            
    answer = 0
    while stack:
        now = stack.pop()
        visited[now] = True
        for check in graph[now]:
            if visited[check]:
                continue
            else:
                dic[check] -= 1
                answer += abs(a[now])
                a[check] += a[now]
                if dic[check] == 1:
                    stack.append(check)

    return answer