def solution(n, s):
    num = s // n
    if num == 0:
        return [-1]
    else:
        over = s % n
        answer = [num] * (n - over)
        added = [num + 1] * over
        return answer + added