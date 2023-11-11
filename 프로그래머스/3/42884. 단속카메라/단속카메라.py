def solution(routes):
    routes = sorted(routes, key = lambda x: x[1])
    answer = 1
    s, e = routes[-1]
    for i in range(len(routes)):
        route = routes.pop()
        if route[1] < s:
            
            answer += 1
            s, e = route
        elif s < route[0]:
            s = route[0]
        
    return answer