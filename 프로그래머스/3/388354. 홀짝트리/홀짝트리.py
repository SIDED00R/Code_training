from collections import defaultdict, Counter

def solution(nodes, edges):
    answer = [0, 0]
    
    dic = {}
    for node in nodes:
        dic[node] = 0

    route = defaultdict(list)
    for edge in edges:
        a, b = edge
        route[a].append(b)
        route[b].append(a)
        dic[a] += 1
        dic[b] += 1
        
    visited = Counter(nodes)
    for now_node in nodes:
        if visited[now_node] != 0:
            visited[now_node] = 0
            stack = [now_node]
            check = []
            while stack:
                out = stack.pop()
                if (out % 2) == (len(route[out]) % 2):
                    check.append(True)
                else:
                    check.append(False)
                for next_node in route[out]:
                    if visited[next_node] != 0:
                        visited[next_node] = 0
                        stack.append(next_node)
            if len(check) == 1:
                if check[0]:
                    answer[0] += 1
                else:
                    answer[1] += 1
            elif len(check) == 2:
                if check[0] != check[1]:
                    answer[0] += 1
                    answer[1] += 1
            else:
                if sum(check) == 1:
                    answer[0] += 1
                elif sum(check) == len(check) - 1:
                    answer[1] += 1

    return answer