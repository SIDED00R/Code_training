from collections import deque

t = int(input())

visited = [False] * 1000001
parent = [(-1, -1)] * 1000001 

q = deque([3, 5, 8])
visited[3] = visited[5] = visited[8] = True
parent[3] = (-1, 3)
parent[5] = (-1, 5)
parent[8] = (-1, 8)

while q:
    curr = q.popleft()
    for d in [3, 5, 8]:
        nxt = curr + d
        if nxt <= 1000000 and not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = (curr, d)
            q.append(nxt)

def reconstruct(n):
    if not visited[n]:
        return -1
    result = []
    while n != -1:
        prev, digit = parent[n]
        result.append(str(digit))
        n = prev
    result.reverse()
    return ''.join(sorted(result)) 
for _ in range(t):
    num = int(input())
    res = reconstruct(num)
    print(res)
