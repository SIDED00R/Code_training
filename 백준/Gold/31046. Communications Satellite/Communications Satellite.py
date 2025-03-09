import heapq

def find(node):
    if parent[node] == node:
        return node
    else:
        return find(parent[node])

def union(first, second, count, answer, weight):
    f_p = find(first)
    s_p = find(second)
    if f_p != s_p:
        count += 1
        parent[s_p] = f_p
        return count, answer + weight
    return count, answer

n = int(input())

if n == 1:
    print(0)
    exit()

circle = []
for _ in range(n):
    x, y, r = map(int, input().split())
    circle.append([x, y, r])

line = []
for i in range(n):
    for j in range(i + 1, n):
        ix, iy, ir = circle[i]
        jx, jy, jr = circle[j]
        w = (abs(ix - jx) ** 2 + abs(iy - jy) ** 2) ** 0.5 - ir - jr
        heapq.heappush(line, [w, i, j])

parent = [i for i in range(n)]

count = 0
answer = 0
while True:
    now_w, now_i, now_j = heapq.heappop(line)
    count, answer = union(now_i, now_j, count, answer, now_w)
    if count == n - 1:
        break

print(round(answer, 8))

