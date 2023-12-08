def solution(n, roads, sources, destination):
    connect = [[] for _ in range(n + 1)]
    far = [-1] * (n + 1)
    far[destination] = 0
    
    for first, second in roads:
        connect[first] += [second]
        connect[second] += [first]
    stack = connect[destination]
    new_stack = []
    count = 1
    while stack:
        num = stack.pop()
        if far[num] == -1:
            far[num] = count
            for case in connect[num]:
                if far[case] == -1:
                    new_stack.append(case)
        if stack == []:
            count += 1
            stack = new_stack[:]
            new_stack = []
            
    return [far[source] for source in sources]