def solution(s):
    stack = []
    for alp in s:
        if len(stack) != 0 and stack[-1] == alp:
            stack.pop()
        else:
            stack.append(alp)

    return 1 if len(stack) == 0 else 0