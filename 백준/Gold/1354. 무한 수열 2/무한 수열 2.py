from collections import defaultdict
import heapq, math

n, p, q, x, y = map(int, input().split())
if n == 0:
    print(1)
    exit()
dic = defaultdict(int)
dic[n] += 1
heap = []
heapq.heappush(heap, -n)
while heap:
    out = -heapq.heappop(heap)
    weight = dic[out]
    dic[out] = 0
    f = math.floor(out / p) - x
    s = math.floor(out / q) - y
    if f > 0 and f not in dic:
        heapq.heappush(heap, -f)
    if s > 0 and s not in dic:
        heapq.heappush(heap, -s)
    dic[max(0, f)] += weight
    dic[max(0, s)] += weight

print(dic[0])