def solution(n, wires):
    answer = n

    for i in range(n):
        count = 0
        ltree = set()
        tree = [[] for _ in range(n)]
        for node1, node2 in wires[:i] + wires[i + 1:]:
            tree[node1 - 1].append(node2 - 1)
            tree[node2 - 1].append(node1 - 1)
        if tree[0] == []:
            if answer > n - 2:
                answer = n - 2
        else:
            stack = []
            stack.append(0)
            while stack:
                now = stack.pop(0)
                ltree.add(now)
                for i in range(len(tree[now])):
                    stack.append(tree[now].pop())
            
            count = len(ltree)
            if count > n - count:
                if answer > 2 * count - n:
                    answer = 2 * count - n
            else:
                if answer > n - 2 * count:
                    answer = n - 2 * count

    return answer