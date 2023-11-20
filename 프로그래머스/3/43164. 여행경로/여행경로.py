import sys
sys.setrecursionlimit(10000)

def find(dic, start, count, N, answer, route):
    if N == count:
        answer.append(route[:])
        return
    
    elif start not in dic or dic[start] == []:
        return
    
    for idx in range(len(dic[start])):
        now = dic[start][idx]
        front = dic[start][:idx]
        back = dic[start][idx + 1:] 
        dic[start] = front + back
        route.append(now)
        find(dic, now, count + 1, N, answer, route)
        route.pop()
        dic[start] = front + [now] + back
    return

def solution(tickets):
    dic = {}
    for ticket in tickets:
        if ticket[0] in dic:
            dic[ticket[0]] += [ticket[1]]
        else:
            dic[ticket[0]] = [ticket[1]]
    
    N = len(tickets)
    answer = []
    route = ["ICN"]
    find(dic, "ICN", 0, N, answer, route)
    
    if len(answer) == 1:
        return answer[0]
    else:
        for idx in range(len(answer)):
            answer[idx] = "".join(answer[idx])
        
        answer = sorted(answer)
        return [answer[0][i:i + 3] for i in range(0, len(answer[0]), 3)]