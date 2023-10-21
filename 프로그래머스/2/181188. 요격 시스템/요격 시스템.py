def solution(targets):
    targets = sorted(targets, key = lambda x: [x[1], x[0]])
    left, right = targets.pop()
    answer = 1
    while targets:
        l, r = targets.pop()
        if left >= r:
            answer += 1
            left = l
            right = r
        elif left <= l:
            left = l
            right = r
        else:
            right = r
            
    return answer