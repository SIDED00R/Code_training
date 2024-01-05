import sys
input = sys.stdin.readline

import heapq

N = int(input())

heap = []
for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(heap, [end, start])

count = 0
now = - 1
while heap:
    next_now_end, next_now_start = heapq.heappop(heap)
    if next_now_start >= now:
        count += 1
        now = next_now_end

print(count)