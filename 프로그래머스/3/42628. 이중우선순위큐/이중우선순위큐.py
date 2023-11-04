import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    dic = {}
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        else:
            if num == -1:
                while min_heap:
                    min_value = heapq.heappop(min_heap)
                    if dic[min_value] == 0:
                        continue
                    else:
                        dic[min_value] -= 1
                        break
            else:
                while max_heap:
                    max_value = -heapq.heappop(max_heap)
                    if dic[max_value] == 0:
                        continue
                    else:
                        dic[max_value] -= 1
                        break
    
    answer = []        
    
    while max_heap:
        max_value = -heapq.heappop(max_heap)
        if dic[max_value] == 0:
            continue
        else:
            answer.append(max_value)
            break
    while min_heap:
        min_value = heapq.heappop(min_heap)
        if dic[min_value] == 0:
            continue
        else:
            answer.append(min_value)
            break
    
    return answer if answer else [0, 0]
    