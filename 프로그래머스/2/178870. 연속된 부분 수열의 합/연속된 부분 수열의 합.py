from collections import deque

def solution(sequence, k):
    case = deque([])
    total = 0
    answer = []
    answer_len = 1e9
    for idx, num in enumerate(sequence):
        if total < k:
            case.append(num)
            total += num
        while total > k:
            out = case.popleft()
            total -= out
        if total == k:
            if answer_len > len(case):
                answer_len = len(case)
                answer = [idx - answer_len + 1, idx]
            if case != []:
                out = case.popleft()
                total -= out
                
    return answer