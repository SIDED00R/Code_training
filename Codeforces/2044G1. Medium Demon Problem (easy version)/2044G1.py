def find_cycle(arr):
    n = len(arr)
    visited = [0] * n
    result = []
    
    for idx in range(n):
        if visited[idx] != 0:
            continue
        path = []
        path_index = {}
        node = idx
        
        while visited[node] == 0:
            visited[node] = 1
            path_index[node] = len(path)
            path.append(node)
            node = arr[node] - 1
        if visited[node] == 1:
            start = path_index[node]
            result.extend(path[start:])
        for p in path:
            visited[p] = 2
    return result
    
def move(arr, node, s):
    count = 2
    while node not in s:
        count += 1
        node = arr[node] - 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    move_list = [0] * n
    for idx in line:
        move_list[idx - 1] = 1
    check_point = []
    for i in range(n):
        if move_list[i] == 0:
            check_point.append(i)
            
    if not check_point:
        print(2)
        continue
    cycle = set(find_cycle(line))
    
    answer = 2
    for now in check_point:
        answer = max(answer, move(line, now, cycle))
    print(answer)