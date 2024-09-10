import heapq
from collections import defaultdict
n = int(input())
score = []
dic = defaultdict(int)
for _ in range(n):
    c, n, s = map(int, input().split())
    heapq.heappush(score, [-s, c, n])

for _ in range(3):
    s, c, n = heapq.heappop(score)
    while dic[c] == 2:
        s, c, n = heapq.heappop(score)
    dic[c] += 1
    print(f"{c} {n}")