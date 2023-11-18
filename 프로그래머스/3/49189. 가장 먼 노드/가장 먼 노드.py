def solution(n, vertex):
    nodes = ["X"] * (n + 1)
    arr = [[] for _ in range(n + 1)]
    for v in vertex:
        i, j = v
        arr[i] += [j]
        arr[j] += [i]
    
    count = 0
    stack = [1]
    while stack:
        new_stack = []
        count += 1
        while stack:
            num = stack.pop()
            if nodes[num] == "X":
                nodes[num] = count
                new_stack += arr[num]
        stack = new_stack[:]
    return nodes.count(count - 1)