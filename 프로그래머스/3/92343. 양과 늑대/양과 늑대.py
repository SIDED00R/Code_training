import sys
sys.setrecursionlimit(10**9)
max_value = 0

def find_case(info, able, tree, stack, count):
    global max_value
    now_is_sheep = False
    if len(stack) == 1:
        now = stack.pop()
        if info[now] == 0:
            now_is_sheep = True
            count += 1
            able += 1
            if count > max_value:
                max_value = count
        else:
            able -= 1
        if len(tree[now]) == 0 or able == 0:
            if now_is_sheep:
                count -= 1
                able -= 1
            else:
                able += 1
            stack = [now]
            return 
        stack = tree[now][:]
        find_case(info, able, tree, stack, count)
        if now_is_sheep:
            count -= 1
            able -= 1
        else:
            able += 1
        stack = [now]
    else:
        for i in range(len(stack)):
            now = stack[i]
            front = stack[:i]
            back = stack[i + 1:]
            now_next = tree[now][:]
            if info[now] == 0:
                now_is_sheep = True
                able += 1
                count += 1
                if count > max_value:
                    max_value = count
            else:
                able -= 1
            if able == 0:
                stack = front + [now] + back
                able += 1
            else:
                find_case(info, able, tree, front + back + now_next, count)
                if now_is_sheep:
                    count -= 1
                    able -= 1
                else:
                    able += 1
                stack = front + [now] + back
    return

    

def solution(info, edges):
    global max_value
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        before, after = edge
        tree[before].append(after)
    stack = [0]
    able = 0
    count = 0
    find_case(info, able, tree, stack, count)
            
    return max_value