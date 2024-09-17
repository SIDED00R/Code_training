import heapq
heap = []
for idx in range(8):
    num = int(input())
    heapq.heappush(heap, [-num, idx + 1])

answer = 0
answer_idx = []
for _ in range(5):
    now_num, now_idx = heapq.heappop(heap)
    answer -= now_num
    answer_idx.append(now_idx)
    
answer_idx = sorted(answer_idx)
print(answer)
for num in answer_idx:
    print(num, end = " ")