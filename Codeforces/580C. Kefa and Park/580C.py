from collections import defaultdict
n, m = map(int, input().split())
cat = list(map(int, input().split()))
route = defaultdict(list)
for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    route[x].append(y)
    route[y].append(x)
    
visited = [-1] * n
visited[0] = cat[0]
stack = [0]
answer = 0
while stack:
    out = stack.pop()
    weight = visited[out]
    count = 0
    for next_node in route[out]:
        if visited[next_node] != -1:
            continue
        else:
            count += 1
            if cat[next_node] == 0:
                visited[next_node] = 0
                stack.append(next_node)
            else:
                visited[next_node] = weight + cat[next_node]
                if visited[next_node] > m:
                    continue
                stack.append(next_node)
                
    if count == 0:
        answer += 1

print(answer)