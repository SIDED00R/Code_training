import heapq
def solution(lines):
    front_heap = []
    back_heap = []
    for line in lines:
        days, time, long = line.split()
        h, m, ss = time.split(":")
        s, ms = ss.split(".")
        long = long[:-1].split(".")
        if len(long) == 1:
            long_s = int(long[0])
            long_ms = 0
        else:
            long_s = int(long[0])
            long_ms = int(long[1].ljust(3, "0"))

        end_s = int(h) * 60 * 60 + int(m) * 60 + int(s)
        end_ms = int(ms.ljust(3, "0"))
        
        start_s = end_s - long_s
        start_ms = end_ms - long_ms + 1
        if start_ms < 0:
            start_ms += 1000
            start_s -= 1
        elif start_ms >= 1000:
            start_ms -= 1000
            start_s += 1
        heapq.heappush(front_heap, [start_s * 1000 + start_ms, end_s * 1000 + end_ms])
    
    count = 0
    answer = 0
    if front_heap[0][0] <= 0:
        now_time = 0
    else:
        now_time = front_heap[0][0]
    while front_heap:
        while front_heap and now_time >= front_heap[0][0]:
            start_time, end_time = heapq.heappop(front_heap)
            count += 1
            heapq.heappush(back_heap, end_time)
        if answer < count:
            answer = count
        if front_heap:
            if back_heap and front_heap[0][0] >= back_heap[0] + 1000:
                now_time = back_heap[0] + 1000
            else:
                now_time = front_heap[0][0]
                continue
        while back_heap and now_time >= back_heap[0] + 1000:
            heapq.heappop(back_heap)
            count -= 1
        
    return answer