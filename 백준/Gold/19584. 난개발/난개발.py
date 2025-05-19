n, m = map(int, input().split())

dic = {}
for idx in range(n):
    x, y = map(int, input().split())
    dic[idx + 1] = y

events = []
for _ in range(m):
    u, v, c = map(int, input().split())
    y1, y2 = sorted([dic[u], dic[v]])
    events.append((y1, c)) 
    events.append((y2, -c))

events.sort(key=lambda x: (x[0], -x[1]))

max_weight = 0
current_weight = 0

for y, delta in events:
    current_weight += delta
    max_weight = max(max_weight, current_weight)

print(max_weight)
