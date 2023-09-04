def solution(num, total):
    n = total // num
    ran = num // 2
    if num % 2 == 0:
        return list(range(n - ran + 1, n + ran + 1))
    else:
        return list(range(n - ran, n + ran + 1))
    return answer