import heapq

def solution(n, k, enemy):
    heap = []
    total = 0
    count = 0
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        total += enemy[i]
        if total > n:
            if k == 0:
                break
            else:
                k -= 1
                card = heapq.heappop(heap)
                total += card
        count += 1
        
    return count
