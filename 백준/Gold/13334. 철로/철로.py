import heapq

n = int(input())
stack = []
for _ in range(n):
    h, o = map(int, input().split())
    h, o = min(h, o), max(h, o)
    stack.append([h, o, o - h])

d = int(input())

heap_stack = []
for now_case in stack:
    h, o, length = now_case
    if length <= d:
        heapq.heappush(heap_stack, [o, h])

answer = 0
if heap_stack:
    now_end = heap_stack[0][0]
    now_point = now_end - d
    now_stack = []
    
    while heap_stack:
        o, h = heapq.heappop(heap_stack)
        if now_end < o:
            now_point = o - d
            now_end = o
            while now_stack:
                if now_stack[0][0] < now_point:
                    heapq.heappop(now_stack)
                else:
                    break
        heapq.heappush(now_stack, [h, o])
        answer = max(answer, len(now_stack))

print(answer)
    