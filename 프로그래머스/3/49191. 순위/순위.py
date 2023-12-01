def solution(n, results):
    front = [[] for _ in range(n)]
    back = [[] for _ in range(n)]
    for first, second in results:
        front[second - 1] += [first - 1]
        back[first - 1] += [second - 1]
    for case in [front, back]:
        for i, node in enumerate(case):
            stack = node[:]
            
            while stack:
                new = stack.pop()
                for num in case[new]:
                    if not num in node:
                        stack.append(num)
                        case[i] += [num]

    answer = 0
    for i in range(n):
        if len(front[i]) + len(back[i]) == n - 1:
            answer += 1
    
    return answer