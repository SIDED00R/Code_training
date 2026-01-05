from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def find(s, t, n, dic):
    visited = [0 for _ in range(n + 1)]
    visited[s] = 1
    answer = 1e10
    stack = deque([s])
    while stack:
        out = stack.popleft()
        if out == t:
            answer = visited[out]
            break
        for next_node in dic[out]:
            if not visited[next_node]:
                visited[next_node] = visited[out] + 1
                stack.append(next_node)
    return answer
while True:
    n = int(input())
    if n == 0:
        break
    s, t = map(int, input().split())
    m = int(input())
    road = []
    dic = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        road.append([a, b])
        dic[a].append(b)
    
    answer = find(s, t, n, dic)
    answer_idx = 0
    
    for idx in range(m):
        a, b = road[idx]
        dic[a].remove(b)
        dic[b].append(a)
        now = find(s, t, n ,dic)
        if now < answer:
            answer = now
            answer_idx = idx + 1
        dic[b].remove(a)
        dic[a].append(b)
    
    print(answer - 1, answer_idx)