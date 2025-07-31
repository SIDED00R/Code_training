import heapq
import sys
sys.setrecursionlimit(100000)

def find(num):
    if parent[num] != num:
        parent[num] = find(parent[num])
    return parent[num]
        
def union(a, b):
    a_p = find(a)
    b_p = find(b)
    if a_p == b_p:
        return False
    else:
        if a_p < b_p:
            parent[b_p] = a_p
        else:
            parent[a_p] = b_p
        return True


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

stack = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(stack, [c, a, b])

answer = 0
count = 0
while stack:
    if count == v - 1:
        break
    c, a, b = heapq.heappop(stack)
    if union(a, b):
        answer += c
        count += 1

print(answer)