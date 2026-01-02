from collections import defaultdict
import heapq, math

n, p, q = map(int, input().split())
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
    f = math.floor(out / p)
    s = math.floor(out / q)
    if f != 0 and f not in dic:
        heapq.heappush(heap, -f)
    if s != 0 and s not in dic:
        heapq.heappush(heap, -s)
    dic[f] += weight
    dic[s] += weight

print(dic[0])