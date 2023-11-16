from collections import deque

def solution(gems):
    N = len(set(gems))
    dic = {}
    dq = deque()
    total = 0
    first, end = 0, 0
    answer = []
    
    for gem in gems:
        if gem in dic:
            if dic[gem] == 0:
                total += 1
            dic[gem] += 1
        else:
            dic[gem] = 1
            total += 1
            
        dq.append(gem)
        end += 1
        
        while total == N:
            first += 1
            out = dq.popleft()
            dic[out] -= 1
            if dic[out] == 0:
                total -= 1
            if answer == []:
                answer = [first, end]
            else:
                if answer[1] - answer[0] > end - first:
                    answer = [first, end]
        
    return answer