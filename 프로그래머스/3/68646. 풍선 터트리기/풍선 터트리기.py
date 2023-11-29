import heapq

def solution(a):
    heap = []
    dic = {}
    right = []
    answer = 1
    for num in a:
        heapq.heappush(heap, num)
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
            
    l_min = heap[0]
    r_min = a[-1]
    for i in range(len(a) - 1):
        n = a.pop()
        dic[n] -= 1
        if n < r_min:
            r_min = n
        if n == heap[0]:
            while heap and dic[heap[0]] == 0:
                heapq.heappop(heap)
            l_min = heap[0]
        if not (n > l_min and n > r_min):
            answer += 1
    
    return answer