from collections import defaultdict, deque

def solution(n, lighthouse):
    dic = defaultdict(int)
    nodes = [[] for _ in range(n + 1)]
    light_on = [False] * (n + 1)
    bright = [False] * (n + 1)
    for case in lighthouse:
        a, b = case
        dic[a] += 1
        dic[b] += 1
        nodes[a].append(b)
        nodes[b].append(a)
    end_points = deque()
    for key, value in dic.items():
        if value == 1:
            end_points.append(key)
            
    answer = 0        
    while end_points:
        now_node = end_points.popleft()
        if light_on[now_node]:
            continue
        next_nodes = nodes[now_node]
        for next_node_idx in next_nodes:
            if not light_on[next_node_idx]:
                bright[next_node_idx] = True
                light_on[next_node_idx] = True
                answer += 1
                for case in nodes[next_node_idx]:
                    bright[case] = True
                    dic[case] -= 1
                    if dic[case] == 1:
                        end_points.append(case)

    return answer