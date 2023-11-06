import heapq

def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
        
    for i in range(n):
        num = -heapq.heappop(heap)
        num -= 1
        heapq.heappush(heap, -num)
        
    answer = 0
    for time in heap:
        if time < 0:
            answer += time ** 2

    return answer