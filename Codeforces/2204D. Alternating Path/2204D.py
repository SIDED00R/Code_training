from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    answer = 0
    n, m = map(int, input().split())
    route = defaultdict(list)
    simbol = [-1] * (n + 1)
    for _ in range(m):
        v, u = map(int, input().split())
        route[v].append(u)
        route[u].append(v)
    visited = [False] * (n + 1)
    for idx in range(1, n + 1):
        dic = {0:0, 1:0}
        if not visited[idx]:
            visited[idx] = True
            simbol[idx] = 0
            dic[0] += 1
            stack = [idx]
            able = True
            while stack:
                out = stack.pop()
                for next_node in route[out]:
                    if visited[next_node]:
                        if simbol[next_node] == simbol[out]:
                            able = False
                    else:
                        visited[next_node] = True
                        simbol[next_node] = (simbol[out] + 1) % 2
                        dic[(simbol[out] + 1) % 2] += 1
                        stack.append(next_node)
            if able:
                answer += max(dic[0], dic[1])
    print(answer)