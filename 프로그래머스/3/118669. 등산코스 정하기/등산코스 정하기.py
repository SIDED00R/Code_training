import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    node = ["r"] * (n + 1)
    visit = [False] * (n + 1)
    
    for path in paths:
        i, j ,w = path
        graph[i].append([j, w])
        graph[j].append([i, w])
        
    for gate in gates:
        node[gate] = "g"
    for summit in summits:
        node[summit] = "s"
        
    answer = 10000001
    if len(gates) < len(summits):
        for start in gates:
            visited = visit[:]
            max_weight = 0
            heap = []
            heapq.heappush(heap, [0, start])
            not_find = True
            while not_find and heap:
                now_weight, now = heapq.heappop(heap)
                if not visited[now]:
                    visited[now] = True
                else:
                    continue
                if now_weight > max_weight:
                    max_weight = now_weight
                if node[now] == "s":
                    not_find = False
                    if answer > max_weight:
                        answer = max_weight
                        answer_idx = now
                    elif answer == max_weight and answer_idx > now:
                        answer_idx = now
                    break
                for next_node in graph[now]:
                    node_idx, weight = next_node
                    if not visited[node_idx] and node[node_idx] != "g":
                        heapq.heappush(heap, [weight, node_idx])
    else:
        for start in summits:
            visited = visit[:]
            max_weight = 0
            heap = []
            heapq.heappush(heap, [0, start])
            not_find = True
            while not_find and heap:
                now_weight, now = heapq.heappop(heap)
                if not visited[now]:
                    visited[now] = True
                else:
                    continue
                if now_weight > max_weight:
                    max_weight = now_weight
                if node[now] == "g":
                    not_find = False
                    if answer > max_weight:
                        answer = max_weight
                        answer_idx = start
                    elif answer == max_weight and answer_idx > start:
                        answer_idx = start
                    break
                for next_node in graph[now]:
                    node_idx, weight = next_node
                    if not visited[node_idx] and node[node_idx] != "s":
                        heapq.heappush(heap, [weight, node_idx])

    return [answer_idx, answer]
