import heapq

n = int(input())
time = []
for _ in range(n):
    _, s, e = map(int, input().split())
    time.append([s, e])

time.sort()

answer = 0
heap = []
for idx in range(n):
    now_s, now_e = time[idx]
    while heap and heap[0] <= now_s:
        heapq.heappop(heap)
    heapq.heappush(heap, now_e)
    answer = max(answer, len(heap))
print(answer)