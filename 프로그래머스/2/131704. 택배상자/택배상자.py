def solution(order):
    stack = []
    idx = 0
    for i in range(1, len(order) + 1):
        if order[idx] == i:
            idx += 1
        elif stack == [] or stack[-1] != order[idx]:
            stack.append(i)

        while stack != [] and stack[-1] == order[idx]:
            stack.pop()
            idx += 1

    return idx