def check(tree, weight, color):
    # color: 0 -> w, 1 -> b
    answer = 0
    stack = [[0, color]]
    answer += weight[0][color]
    
    while stack:
        node, c = stack.pop()
        nc = (c + 1) % 2
        for next_node in tree[node]:
            stack.append([next_node, nc])
            answer += weight[next_node][nc]
    return answer
        

n = int(input())
child_tree = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = map(int , input().split())
    child_tree[p].append(c)

weight = []
for _ in range(n):
    w, b = map(int, input().split())
    weight.append([w, b])

print(min(check(child_tree, weight, 0), check(child_tree, weight, 1)))