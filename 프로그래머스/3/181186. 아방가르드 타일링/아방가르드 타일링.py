def solution(n):
    stack = {0 : 1}
    remain = [0, 0, 0]
    for i in range(1, n + 1):
        if i == 1:
            stack[1] = 1
        elif i == 2:
            stack[2] = 3
        elif i == 3:
            stack[3] = 10
        else:
            now = (stack[i - 1] + 2 * stack[i - 2] + 5 * stack[i - 3])
            r = (i - 4) % 3
            if r == 0:
                stack[i] = (now + 2 * remain[0] + 2 * remain[2] + 4 * remain[1]) % 1000000007
            elif r == 1:
                stack[i] = (now + 2 * remain[1] + 2 * remain[0] + 4 * remain[2]) % 1000000007
            elif r == 2:
                stack[i] = (now + 2 * remain[2] + 2 * remain[1] + 4 * remain[0]) % 1000000007
        if i >= 3:
            remain[i % 3] += stack[i - 3]

    return stack[n]