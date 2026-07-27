import heapq
from collections import defaultdict

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def solution(land, height):
    col = len(land)
    row = len(land[0])
    visited = [[0 for _ in range(row)] for _ in range(col)]
    now_count = 0
    for i in range(col):
        for j in range(row):
            if not visited[i][j]:
                now_count += 1
                visited[i][j] = now_count
                stack = [[i, j]]
                while stack:
                    now_i, now_j = stack.pop()
                    now_value = land[now_i][now_j]
                    for idx in range(4):
                        ni = now_i + di[idx]
                        nj = now_j + dj[idx]
                        if 0 <= ni < col and 0 <= nj < row and not visited[ni][nj] and abs(land[ni][nj] - now_value) <= height:
                            visited[ni][nj] = now_count
                            stack.append([ni, nj])
    dic = {}
    route = defaultdict(list)
    for i in range(col):
        for j in range(row):
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if 0 <= ni < col and 0 <= nj < row and visited[i][j] != visited[ni][nj]:
                    a, b = min(visited[i][j], visited[ni][nj]), max(visited[i][j], visited[ni][nj])
                    route[a].append(b)
                    route[b].append(a)
                    if (a, b) in dic:
                        dic[(a, b)] = min(dic[(a, b)], abs(land[i][j] - land[ni][nj]))
                    else:
                        dic[(a, b)] = abs(land[i][j] - land[ni][nj])

    answer = 0
    visited_node = [False] * (now_count + 1)
    visited_node[1] = True
    heap = []
    for next_node in route[1]:
        a, b = 1, next_node
        heapq.heappush(heap, [dic[(a, b)], next_node])
    
    while heap:
        cost, now_node = heapq.heappop(heap)
        if visited_node[now_node]:
            continue
        visited_node[now_node] = True
        answer += cost
        
        for next_node in route[now_node]:
            if not visited_node[next_node]:
                a, b = min(now_node, next_node), max(now_node, next_node)
                heapq.heappush(heap, [dic[(a, b)], next_node])
    return answer

