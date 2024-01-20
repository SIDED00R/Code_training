import heapq
from collections import defaultdict

def time_check(case, reqs):
    wait_total_time = 0
    working = defaultdict(list)
    waiting = defaultdict(list)
    time = 0
    for req in reqs:
        a, b, c = req
        time = a
        if case[c - 1] != -1:
            case[c - 1] -= 1
            heapq.heappush(working[c - 1], time + b)
        else:
            heapq.heappush(waiting[c - 1], [a, b])
            while working[c - 1] and working[c - 1][0] <= time:
                working_out = heapq.heappop(working[c - 1])
                case[c - 1] += 1
                if waiting[c - 1]:
                    waiting_out = heapq.heappop(waiting[c - 1])
                    wait_time = max(working_out - waiting_out[0], 0)
                    wait_total_time += wait_time
                    heapq.heappush(working[c - 1], sum(waiting_out) + wait_time)
                    case[c - 1] -= 1
                    
    for key, values in waiting.items():
        while values:
            waiting_out = heapq.heappop(values)
            if case[key] != -1:
                case[key] -= 1
                continue
            else:
                working_out = heapq.heappop(working[key])
                wait_time = max(working_out - waiting_out[0], 0)
                wait_total_time += wait_time
                heapq.heappush(working[key], sum(waiting_out) + wait_time)
    return wait_total_time
        
def solution(k, n, reqs):
    possible_case = [[]]
    
    for _ in range(k - 1):
        new_possible_case = []
        for case in possible_case:
            total = sum(case)
            for left in range(n - k - total + 1):
                new_possible_case.append(case + [left])
        possible_case = new_possible_case[:]
    for idx, case in enumerate(possible_case):
        total = sum(case)
        possible_case[idx] += [n - k - total]    
    
    min_waiting_time = 1e9
    for case in possible_case:     
        min_waiting_time = min(time_check(case, reqs), min_waiting_time)

    return min_waiting_time