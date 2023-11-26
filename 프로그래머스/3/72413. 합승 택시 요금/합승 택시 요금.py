def solution(n, s, a, b, fares):
    nodes = [[] for _ in range(n)]
    roads = [[0 for _ in range(n)] for _ in range(n)]
    for fare in fares:
        first, second, num = fare
        nodes[first - 1] += [second - 1]
        roads[first - 1][second - 1] = num
        nodes[second - 1] += [first - 1]
        roads[second - 1][first - 1] = num
    
    answer = 100000 * n * n
    for i in range(n):
        count = ["X" for _ in range(n)]
        count[i] = 0
        stack = [i]
        while stack:
            new_stack = []
            while stack:
                now = stack.pop()
                for j in nodes[now]:
                    if count[j] == "X" or count[j] > count[now] + roads[now][j]:
                        if j not in new_stack:
                            new_stack.append(j)
                        count[j] = count[now] + roads[now][j]
            stack = new_stack[:]
        if count[a - 1] == "X" or count[b - 1] == "X" or count[s - 1] == "X":
            continue
        elif answer > count[a - 1] + count[b - 1] + count[s - 1]:
            answer = count[a - 1] + count[b - 1] + count[s - 1]
        
    return answer