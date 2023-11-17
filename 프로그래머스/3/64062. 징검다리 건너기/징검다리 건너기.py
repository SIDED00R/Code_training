from collections import deque
import heapq

def solution(stones, k):
    heap = []
    dq = deque()
    dic = {}
    for stone in stones[:k]:
        heapq.heappush(heap, -stone)
        dq.append(stone)
        if stone in dic:
            dic[stone] += 1
        else:
            dic[stone] = 1
    answer = -heap[0]
    for stone in stones[k:]:
        heapq.heappush(heap, -stone)
        dq.append(stone)
        if stone in dic:
            dic[stone] += 1
        else:
            dic[stone] = 1
            
        out = dq.popleft()
        dic[out] -= 1
        if out == -heap[0]:
            while True:
                large = -heap[0]
                if dic[large] == 0:
                    heapq.heappop(heap)
                    continue
                else:
                    break
            if answer > -heap[0]:
                answer = -heap[0]

    return answer