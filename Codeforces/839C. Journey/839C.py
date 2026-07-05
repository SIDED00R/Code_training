from collections import defaultdict

n = int(input())
route = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    route[u].append(v)
    route[v].append(u)
    
visited = [False] * (n + 1)
visited[1] = True
stack = [[1, 1, 0]]
answer = 0
while stack:
    idx, p, l = stack.pop()
    next_length = 0
    for next_idx in route[idx]:
        if not visited[next_idx]:
            next_length += 1
    if next_length == 0:
        answer += p * l
    else:
        for next_idx in route[idx]:
            if not visited[next_idx]:
                visited[next_idx] = True
                stack.append([next_idx, p / next_length, l + 1])
print(answer)