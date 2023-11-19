def union(parent, first, second):
    f = find_parent(parent, first)
    s = find_parent(parent, second)
    if f < s:
        parent[s] = f
    else:
        parent[f] = s

def find_parent(parent, node):
    if parent[node] == node:
        return node
    return find_parent(parent, parent[node])

def able(parent, first, second):
    f = find_parent(parent, first)
    s = find_parent(parent, second)
    if f == s:
        return False
    return True

def solution(n, costs):
    answer = 0
    count = 0
    costs = sorted(costs, key = lambda x: x[2])
    parent = [i for i in range(n)]
    for cost in costs: 
        first, second, num = cost
        if able(parent, first, second):
            answer += num
            union(parent, first, second)
            count += 1
        if count == n - 1:
            break
            
    return answer