import heapq
def solution(jobs):
    heap = []
    running = False
    # sort가 필요한 경우 해줌
    jobs = sorted(jobs, key = lambda x:x[0])
    now = jobs[0][0]
    idx = 0
    answer = 0
    N = len(jobs)
    
    while True:
        while idx != N and now >= jobs[idx][0]:
            heapq.heappush(heap,jobs[idx][1])
            idx += 1
            
        if running:
            if len(heap) == 0:
                now = jobs[idx][0]
            else:
                time = heapq.heappop(heap)
                now += time
                answer += now
        else:
            running = True
            time = heapq.heappop(heap)
            now += time
            answer += now
            
        if heap == [] and idx == N:
            break
        
    for job in jobs:
        answer -= job[0]
    return answer // N