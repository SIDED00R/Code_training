import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    total = len(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second * 2
        heapq.heappush(scoville, new)
    return total - len(scoville)