from collections import defaultdict
from itertools import product

def find(n, infect, now_p, route):
    visited = [False] * (n + 1)
    stack = [infect]
    visited[infect] = True
    answer = 1
    for idx, p in enumerate(now_p):
        if idx != 0:
            if p == now_p[idx - 1]:
                continue
        for now_node in stack:
            if (now_node, p) in route:
                for next_node in route[(now_node, p)]:
                    if not visited[next_node]:
                        visited[next_node] = True
                        stack.append(next_node)
                        answer += 1
    return answer

def solution(n, infect, c, k):
    route = defaultdict(list)
    answer = 0
    for now_case in c:
        a, b, s = now_case
        route[(a, s)].append(b)
        route[(b, s)].append(a)
    for now_p in product([1, 2, 3], repeat=k):
        answer = max(answer, find(n, infect, now_p, route))
    return answer
